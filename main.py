import google.generativeai as genai

genai.configure(api_key="AIzaSyDqbxH25SzLXPUe3T-eMsvBxKiB_9cht3c")

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("AIzaSyDqbxH25SzLXPUe3T-eMsvBxKiB_9cht3c")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")  # or 2.0 if available
chat = model.start_chat(history=[])
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)
