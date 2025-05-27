from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    return jsonify({"status": "success", "message": f"Thank you {name}, we'll be in touch!"})

if __name__ == "__main__":
    app.run(debug=True)
