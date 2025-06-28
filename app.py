from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)
users = {}  # vaqtincha xotirada foydalanuvchilar saqlanadi

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if username not in users:
        return jsonify({'message': 'User not found'}), 404

    hashed = users[username]
    if bcrypt.checkpw(password.encode('utf-8'), hashed):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
