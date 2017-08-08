from flask import Flask, send_file, jsonify, request

import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see

app = Flask(__name__)
app.use_reloader=False

@app.route("/")
def hello():
    return "Hello, je suis GENIAL-O"

@app.route("/detect")
def get_distances():
    return jsonify(
        front=detect.get_front_distance(),
        left=detect.get_left_distance(),
        right=detect.get_right_distance(),
        back=detect.get_back_distance(),
    )

@app.route("/camera")
def get_camera_image():
    return send_file(see.LATEST_PIC_PATH, mimetype="image/jpg")

@app.route("/print", methods=["POST"])
def print_text():
    text=request.form["text"]
    line=int(float(request.form["line"]))
    display.print_text(text, line)
    return "OK"

@app.route("/talk", methods=["POST"])
def make_talk():
    text=request.form["text"]
    speak.talk(text)
    return "OK"

@app.route("/pilot", methods=["PUT"])
def set_auto_pilot():
    auto_pilot=request.form["auto_pilot"]
    move.set_auto_pilot(auto_pilot)
    return "OK"

@app.route("/move", methods=["POST"])
def make_move():
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
    return "OK"

@app.route("/stop", methods=["POST"])
def stop():
    move.stop()
    return "OK"
