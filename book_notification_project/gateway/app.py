from flask import Flask, request, jsonify, Response
import requests
from flask_cors import CORS, cross_origin

ESTANTES = "http://localhost:8000/api/estantes/"
USUARIOS = "http://localhost:8000/api/usuarios/"
LIVROS = "http://localhost:8000/api/livros"
BOOKS = "https://www.googleapis.com/books/v1/volumes"

app = Flask(__name__)
cors = CORS(app)


def api_online(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return False
    return True

@app.get("/")
def root():
    return jsonify({
        "_links": {
            "self": {"href": "http://localhost:5000"},
            "usuarios": {"href": "http://localhost:5000/usuarios"},
            "estantes": {"href": "http://localhost:5000/estantes"},
            "livros": {"href": "http://localhost:5000/livros"},
            "books": {"herf":"https://www.googleapis.com/books/v1/volumes/"}
        }
    }), 200

@app.route("/estantes", methods = ["GET","POST"])
def estantes():
    if not api_online(ESTANTES):
        return Response("api offline", status = 502)
    if request.method == "GET" :
        resposta = requests.get(ESTANTES)
        return Response(resposta.text, status = 200, mimetype ="application/json")
    
@app.route("/estantes/<int:usuario_id>", methods=["POST"])
def add_to_estante(usuario_id):
    if not api_online(ESTANTES):
        return Response("api offline", status=502)
    data = request.get_json()
    livro = {
        "titulo": data.get("titulo"),
        "descricao": data.get("descricao"),
        "autores": data.get("autores")
    }
    resposta = requests.post(f"{ESTANTES}{usuario_id}/", json=livro)
    return Response(resposta.text, status=resposta.status_code, mimetype="application/json")



@app.route("/livros",methods = ["GET","POST"])
def livros():
    if not api_online(LIVROS):
        return Response("api offline", status = 502)
    if request.method == "GET" :
        resposta = requests.get(ESTANTES)
        return Response(resposta.text, status = 200, mimetype ="application/json")


@app.route("/usuario",methods = ["GET","POST"])
def usuario():
    if not api_online(USUARIOS):
        return Response("api offline", status = 502)
    if request.method == "GET" :
        resposta = requests.get(ESTANTES)
        return Response(resposta.text, status = 200, mimetype ="application/json")
    
@app.route("/books", methods = ["POST"])
def books():
    data = request.get_json()
    search_param = data.get("search_param")
    resposta = requests.get(f"{BOOKS}?q={search_param}")
    return Response (resposta.text, status = 200, mimetype = "application/json")
    


@app.route('/')
def index():
    return jsonify({"message": "API Flask está online!"})

if __name__ == '__main__':
    app.run(debug=True)