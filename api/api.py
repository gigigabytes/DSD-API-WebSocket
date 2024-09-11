from flask import Flask, jsonify, request # type: ignore
import requests

app = Flask(__name__)

# Função de HATEOAS para adicionar links
def add_hateoas_links(base_url, data, entity):
    data['links'] = [
        {'rel': 'self', 'href': f'{base_url}/{entity}/{data["id"]}'},
        {'rel': 'update', 'href': f'{base_url}/{entity}/{data["id"]}/update'},
        {'rel': 'delete', 'href': f'{base_url}/{entity}/{data["id"]}/delete'}
    ]
    return data

# Rota para obter livros da estante de um usuário
@app.route('/users/<int:user_id>/shelf', methods=['GET'])
def get_user_shelf(user_id):
    try:
        response = requests.get(f'http://localhost:5003/users/{user_id}/shelf')
        shelf = response.json()
        hateoas_shelf = [add_hateoas_links(request.base_url, item, 'shelf') for item in shelf]
        return jsonify(hateoas_shelf), 200
    except:
        return jsonify({'error': 'Unable to fetch shelf details'}), 500
    

# Rota para adicionar um livro à estante de um usuário
@app.route('/shelf', methods=['POST'])
def add_book_to_shelf():
    shelf_data = request.json
    try:
        response = requests.post('http://localhost:5003/shelf', json=shelf_data)
        new_shelf_item = response.json()
        hateoas_shelf_item = add_hateoas_links(request.base_url, new_shelf_item, 'shelf')
        return jsonify(hateoas_shelf_item), 201
    except:
        return jsonify({'error': 'Unable to add book to shelf'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
