from flask import Flask, send_file

import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, je suis GENIAL-O"

@app.route("/detect")
def detect():
    return flask.jsonify(
        front=detect.get_front_distance(),
        left=detect.get_left_distance(),
        right=detect.get_right_distance(),
        back=detect.get_back_distance()
    )

@app.route("/camera")
def camera():
    return send_file(see.LATEST_PIC_PATH, mimetype="image/jpg")

@app.route("/print", methods=["POST"])
def print_text():
    text=request.form["text"]
    line=request.form["line"]
    display.print_text(text, line)

@app.route("/talk", methods=["POST"])
def talk():
    text=request.form["text"]
    speak.talk(text)

@app.route("/pilot", methods=["PUT"])
def set_auto_pilot():
    auto_pilot=request.form["auto_pilot"]
    move.set_auto_pilot(auto_pilot)

@app.route("/move", methods=["POST"])
def move():
    speed=request.form["speed"]
    direction=request.form["direction"]
    if direction == "forward":
        move.go_forward(speed)
    elif direction == "rotate_left":
        move.rotate_left(speed)
    elif direction == "rotate_right":
        move.rotate_right(speed)
    elif direction == "backward":
        move.go_backward(speed)

@app.route("/stop", methods=["POST"])
def stop():
    move.stop()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
