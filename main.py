from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)
# all_messages = []
DB_FILE = "db.json"


def load_messages(): #загрузка db.json
    with open(DB_FILE, "r") as json_file:
        data = json.load(json_file)
    return data['messages']

all_messages = load_messages()


def save_messages():
    data = {
        "messages": all_messages
    }
    with open(DB_FILE, 'w') as json_file:
        json.dump(data, json_file)


@app.route("/")
def index_page():
    # return "hello"
    return "Hello  <b>everyone!</b>"


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/chat")
def display_chat():
    return render_template("form.html")


@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    save_messages()
    return "OK"



def add_message(sender, text):
    new_message = {
        "text": text,
        "sender": sender,
        "time": datetime.now().strftime("%H:%M"),
    }

    all_messages.append(new_message)
    save_messages()


app.run(host="0.0.0.0", port=80)