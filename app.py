from flask import Flask, jsonify, request
from utils import process_data

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "API is running"})


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    result = process_data(data["name"])
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)