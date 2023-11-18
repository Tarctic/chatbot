# import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods = ["GET"])
def get_bot_response():
    user_message = request.args.get('msg')
    api_key = ""
    model = "text-davinci-003"
    response = generate_response_gpt3(user_message, model, api_key)
    return response

def generate_response_gpt3(user_message, model, api_key):
    prompt = (f"User: {user_message}\n"
              f"Chatbot: ")
    response = requests.post(
        f"https://api.openai.com/v1/engines/{model}/completions",
        headers = {"Authorization" : f"Bearer {api_key}"},
        json={
            "prompt" : prompt,
            "max_tokens" : 200,
            "temperature": 0.7
        },
    )

    reply = response.json()["choices"][0]["text"].strip()
    return reply


if __name__ == "__main__":
    app.run()