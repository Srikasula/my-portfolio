# 🤖 AI-Powered Full Stack Chatbot

This is a full stack chatbot application built with a Python Flask backend and a simple HTML/JavaScript frontend. It uses OpenAI's GPT API to generate intelligent responses based on user input.

---

## 🔧 Tech Stack

- **Frontend:** HTML, JavaScript, Fetch API
- **Backend:** Python, Flask
- **AI Engine:** OpenAI GPT (via API)

---

## 🛠 How to Run Locally

### 1. Set your OpenAI API key
Edit `app.py` and replace `"YOUR_OPENAI_API_KEY"` with your actual key.

Or securely load it from `.env` (optional later step).

### 2. Run the Flask Backend
```bash
cd chatbot_app/backend
python app.py
