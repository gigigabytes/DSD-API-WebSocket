from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import os

app = FastAPI()

# Obtendo a SECRET_KEY do ambiente ou configurando um fallback padrão
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"

# Configurando o OAuth2 para autenticação com o token JWT do auth_service
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://auth-service/token")

# Banco de dados simulado de livros
books_db = {
    1: {"title": "Livro A", "available": False, "reserved_by": None},
    2: {"title": "Livro B", "available": True, "reserved_by": None}
}

# Função para validar o token JWT
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Endpoint para reservar um livro
@app.post("/reserve/{book_id}")
async def reserve_book(book_id: int, user: str = Depends(get_current_user)):
    book = books_db.get(book_id)
    if book and not book["available"]:
        book["reserved_by"] = user
        return {"message": f"Livro {book['title']} reservado por {user}"}
    return {"error": "Livro não disponível para reserva"}

# Endpoint para devolver um livro
@app.post("/return/{book_id}")
async def return_book(book_id: int, user: str = Depends(get_current_user)):
    book = books_db.get(book_id)
    if book:
        book["available"] = True
        reserved_by = book["reserved_by"]
        book["reserved_by"] = None
        # A lógica de notificação WebSocket poderia ser chamada aqui
        return {"message": f"Livro {book['title']} devolvido"}
    return {"error": "Livro não encontrado"}
