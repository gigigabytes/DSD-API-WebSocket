from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
import jwt  # Certifique-se de que o pacote `pyjwt` está instalado
from jwt import PyJWTError

app = FastAPI()

SECRET_KEY = "gQY8A-PD3E3Nxeay1nZpQeWpbaEbc0mVf8n4ILfzQXk"  # Substitua por sua chave gerada

bearer_scheme = HTTPBearer()

def verificar_jwt(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        return payload
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Token JWT inválido")

@app.get("/livros/")
def obter_livros(credentials: HTTPAuthorizationCredentials = Depends(verificar_jwt)):
    response = requests.get("http://livros_microservico:8000/livros/")
    livros = response.json()
    for livro in livros:
        livro['links'] = {
            'self': f"/livros/{livro['id']}",
            'update': f"/livros/{livro['id']}",
            'delete': f"/livros/{livro['id']}"
        }
    return livros

@app.get("/usuarios/")
def obter_usuarios(credentials: HTTPAuthorizationCredentials = Depends(verificar_jwt)):
    response = requests.get("http://usuarios_microservico:8000/usuarios/")
    usuarios = response.json()
    for usuario in usuarios:
        usuario['links'] = {
            'self': f"/usuarios/{usuario['id']}",
            'update': f"/usuarios/{usuario['id']}",
            'delete': f"/usuarios/{usuario['id']}"
        }
    return usuarios
