from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (from environment variable or hardcoded for testing)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "Chatbot Backend is Running"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use gpt-3.5-turbo if chat model
            prompt=user_message,
            max_tokens=50
        )

        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500
