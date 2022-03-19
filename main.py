from flask import Flask, render_template, request
import datetime
import json

app = Flask(__name__)

def add_message(text, sender):
    if 0<len(text)<=3000 and 2<len(sender)<=100:
        now = datetime.datetime.now()
        time = now.strftime("%H:%M")
        new_message = {"text": text, "sender": sender, "time": time} # ToDO: указать правильную дату
        messages.append(new_message) #Добавляем
    else:
        return print(f"ERROR {len(text)} {len(sender)}")
    save_messages_to_file()

def print_message(message):
    print(f"[{message['sender']}]: {message['time']} / {message['text']}")


messages = []
DB_FILE = "./data/db.json"
db = open(DB_FILE, "rb")
data = json.load(db)
messages = data["messages"]

def save_messages_to_file():
    db = open(DB_FILE, "w")
    data = {"messages": messages}
    json.dump(data, db)

for message in messages:
    print_message(message)

# Main page
@app.route("/")
def index_page():
    return "здравствуйте, это скиллЧат"

#
@app.route("/get_messages")
def get_messages():
    return {"messages": messages}

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/send_message")
def send_message():
    name = request.args["name"]
    text = request.args["text"]
    add_message(text, name)
    return "ok"

app.run()