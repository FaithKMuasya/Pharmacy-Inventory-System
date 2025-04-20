# # from flask import Flask, request, jsonify

# # app = Flask(__name__)

# # # Dummy user data (in a real app, use a database)
# # users = {
# #     "admin": "FaithLoshy",
# #     "kevin": "password24"
# # }

# # @app.route('/login', methods=['POST'])
# # def login():
# #     # Get JSON data from request
# #     data = request.get_json()

# #     username = data.get('username')
# #     password = data.get('password')

# #     # Check if username and password are provided
# #     if not username or not password:
# #         return jsonify({"error": "Username and password are required"}), 400

# #     # Simple authentication check
# #     if username in users and users[username] == password:
# #         return jsonify({"message": "Login successful"}), 200
# #     else:
# #         return jsonify({"error": "Invalid username or password"}), 401

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     return jsonify({"message": f"Received username: {username}, password: {password}"}), 200

# @app.route('/')
# def index():
#     return "Server is running."

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from request
    data = request.get_json()

    # Extract username and password
    username = data.get('username')
    password = data.get('password')

    # Return a response with the received data
    return jsonify({
        "message": f"Received username: {username}, password: {password}"
    }), 200

@app.route('/')
def index():
    return "Server is running."

if __name__ == '__main__':
    app.run(debug=True)

