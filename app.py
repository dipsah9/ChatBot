from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import cohere

# Load environment variables
load_dotenv()

# Get the Cohere API key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY is not set. Please check your .env file.")

# Initialize the Cohere client
co = cohere.Client(COHERE_API_KEY)

# Initialize Flask app
app = Flask(__name__)

# Store chat history
chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        # Generate a response using Cohere
        response = co.generate(
            model="command-xlarge-nightly",
            prompt=user_message,
            max_tokens=50,
            temperature=0.7
        )
        bot_response = response.generations[0].text.strip()
        # Append to chat history
        chat_history.append({"user": user_message, "bot": bot_response})
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": chat_history})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

