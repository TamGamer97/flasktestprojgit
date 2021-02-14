import pyrebase
from flask import Flask, render_template, request, jsonify, redirect, url_for

from fireTam import fw, fr

app = Flask(__name__)

firebaseConfig={
    "apiKey": "AIzaSyCaONijDVn4iPWbqNvOxbRsmVSSjWKUrrQ",
    "authDomain": "fir-flask-testproject.firebaseapp.com",
    "databaseURL": "https://fir-flask-testproject-default-rtdb.firebaseio.com/",
    "projectId": "fir-flask-testproject",
    "storageBucket": "fir-flask-testproject.appspot.com",
    "messagingSenderId": "690973497891",
    "appId": "1:690973497891:web:a3d8861af6ae9151b92f96",
    "measurementId": "G-2E91RJ51S5"
}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

corrUsername = "no user"
corrRoom = "no room"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST", "GET"])
def chat():
    print("loading chat def")

    global corrUsername
    global corrRoom

    username = corrUsername
    room = corrRoom

    return render_template("chat.html", user=username, room=room)

@app.route("/joinroom", methods=["POST", "GET"])
def joinroom():

    global corrUsername
    global corrRoom

    roomName = request.form["Roomname"]
    username = request.form["user"]

    corrUsername = username
    corrRoom = roomName

    print(username + " is joining room " + roomName)

    msg = username + " has joined " + roomName

    loc = roomName + "/messages.txt"

    fw(msg, loc, storage)

    return ""

@app.route("/sendmsg", methods=["POST", "GET"])
def sendmsg():
    print("seding msg")

    msg = request.form["msg"]

    print(msg)

    text = corrUsername + ": " + msg 

    loc = corrRoom + "/messages.txt"

    fw(text, loc, storage)

    return ""

@app.route("/recieveMsgs", methods=["POST", "GET"])
def recieveMsgs():
    print("recieving messages")

    loc = corrRoom + "/messages.txt"

    newMsgs = fr(loc, storage)

    return jsonify(newMsgs)

if(__name__ == "__main__"):
    app.run(debug=False)