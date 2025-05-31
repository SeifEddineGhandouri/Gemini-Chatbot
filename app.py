from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("AIzaSyDzy89AAzhf0lzo6E2YblpIy1eAq3hvYBU")
genai.configure(api_key=api_key)

# Create chatbot instance
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Flask app setup
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["message"]
        response = chat.send_message(user_input)
        return render_template("index.html", user=user_input, bot=response.text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
