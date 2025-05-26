from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or hardcode for testing: openai.api_key = "sk-..."

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
            engine="text-davinci-003",  # Or gpt-3.5-turbo if using chat API
            prompt=user_message,
            max_tokens=50
        )

       

