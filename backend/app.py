
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get Gemini API Key from .env
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY missing in .env file!")

# Gemini API endpoint
# Replace your current GEMINI_URL with this one:
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

print("Chat route loaded")
@app.route("/chat", methods=["POST"])
def chat():
    print("Chat endpoint hit")
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Prepare payload for Gemini
        payload = {
           "contents": [
          {
            "role": "user",
            "parts": [
                {
                    "text": f"You are DharaaBot, a friendly and concise assistant. {user_message}"
                }
            ]
        }
           ]
  }

        # Send request to Gemini API
        response = requests.post(GEMINI_URL, json=payload)
        print("Status:", response.status_code)
        print("Response:", response.text)
        if response.status_code != 200:
            return jsonify({
                "error": f"Gemini API failed: {response.status_code}",
                "details": response.text
            }), response.status_code

        data = response.json()
        ai_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sorry, I couldn’t process that.")

        return jsonify({"reply": ai_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return jsonify({"status": "DharaaBot backend running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
