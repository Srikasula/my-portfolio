from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "Chatbot Backend is Running"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        response = openai.Completion.create(
            engine="text-davinci-003",  # or gpt-3.5-turbo via Chat API
            prompt=user_input,
            max_tokens=50
        )

        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500
