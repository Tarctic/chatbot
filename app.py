# import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template

app = Flask(__name__)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?", "Hey %1 how's ghw going?"]
    ],
    [
        r"what is your name?",
        ["My name is gene", "I'm the cutest bot", "It's nice to meet you, I'm gene"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's ok", "Never gonna give you up, never gonna let you down"]
    ]
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods = ["POST"])
def chat():
    message = request.form["text"]
    response = chatbot.respond(message)
    return response

if __name__ == "__main__":
    app.run()