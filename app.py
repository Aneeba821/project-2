from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend API is working!"})


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400

    return jsonify({
        "message": "User created successfully",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)