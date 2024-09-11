from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'O Senhor dos Anéis', 'author': 'J.R.R. Tolkien'}
]

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)
