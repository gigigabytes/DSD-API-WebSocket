from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'}
]

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)
