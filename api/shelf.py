from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)

# Lista de livros na estante de cada usuário
shelves = [
    {'id': 1, 'user_id': 1, 'book_id': 1, 'read_date': '2024-01-10'},
    {'id': 2, 'user_id': 1, 'book_id': 2, 'read_date': '2024-02-20'},
    {'id': 3, 'user_id': 2, 'book_id': 2, 'read_date': '2024-03-15'}
]

# Endpoint para obter todos os livros da estante de um usuário
@app.route('/users/<int:user_id>/shelf', methods=['GET'])
def get_user_shelf(user_id):
    user_shelf = [shelf for shelf in shelves if shelf['user_id'] == user_id]
    return jsonify(user_shelf), 200

# Endpoint para adicionar um livro à estante de um usuário
@app.route('/shelf', methods=['POST'])
def add_book_to_shelf():
    shelf_data = request.json
    new_shelf_item = {
        'id': len(shelves) + 1,
        'user_id': shelf_data['user_id'],
        'book_id': shelf_data['book_id'],
        'read_date': shelf_data['read_date']
    }
    shelves.append(new_shelf_item)
    return jsonify(new_shelf_item), 201

if __name__ == '__main__':
    app.run(port=5003, debug=True)
