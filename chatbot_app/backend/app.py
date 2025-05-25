from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Serve frontend (index.html) on root route
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

# Chatbot API route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Send message to OpenAI and return the response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port, debug=True)
