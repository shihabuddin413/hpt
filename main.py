import os
import requests
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/', methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    message = data["message"]["text"]
    
    if "hello" in message.lower():
        send_message(chat_id, "Hello! 👋 I'm alive on Render!")
    
    return "ok"

def send_message(chat_id, text):
    requests.post(URL, json={"chat_id": chat_id, "text": text})

@app.route('/')
def home():
    return "Hello Bot is running!"

if __name__ == "__main__":
    app.run(debug=True)
