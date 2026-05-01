from flask import Flask, jsonify, request, render_template
from utils import process_data

app = Flask(__name__)


# 👉 HTML page route
@app.route("/")
def home():
    return render_template("index.html")


# 👉 API route (same as before)
@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    result = process_data(data["name"])
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)