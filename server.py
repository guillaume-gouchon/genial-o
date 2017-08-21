import time
from flask import Flask, send_file, jsonify, request, Response
from flask_cors import CORS
from flask_socketio import SocketIO, emit

import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see
import controllers.status as status
import controllers.recognize as recognize

app = Flask(__name__)
app.use_reloader = False
app.threaded = True
CORS(app)
socketio = SocketIO(app)

def start():
    socketio.run(app, host="0.0.0.0", port=80, log_output=False)

#
# REST routes
#
@app.route("/")
def hello():
    return "Hello, je suis GENIAL-O"

@app.route("/info")
def get_information():
    return jsonify(
        status = status.get_information()
    )

@app.route("/guess")
def guess():
    return jsonify(
        guess = recognize.guess(),
    )

@app.route("/detect")
def get_distances():
    return jsonify(
        front = detect.get_front_distance(),
        left = detect.get_left_distance(),
        right = detect.get_right_distance(),
        back = detect.get_back_distance(),
    )

@app.route("/camera")
def get_camera_image():
    return Response(see.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/last-image")
def get_last_image():
    return send_file(see.LATEST_PIC_PATH, mimetype='image/jpg')

@app.route("/print", methods=["POST"])
def print_text():
    text = request.form["text"]
    line = int(float(request.form["line"]))
    display.clear_text()
    display.print_text(text, line)
    return "OK"

@app.route("/talk", methods=["POST"])
def make_talk():
    text = request.form["text"]
    speak.talk(text)
    return "OK"

@app.route("/pilot", methods=["POST"])
def set_auto_pilot():
    auto_pilot = int(float(request.form["auto_pilot"]))
    move.set_auto_pilot(auto_pilot)
    return "OK"

@app.route("/move", methods=["POST"])
def make_move(speed, direction):
    move.set_auto_pilot(0)
    speed = float(request.form["speed"])
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
    move.set_auto_pilot(0)
    move.stop()
    return "OK"

#
# websockets
#
global nb_ws_connections
nb_ws_connections = 0

@socketio.on('connect')
def socket_join():
    print("client connected")
    global nb_ws_connections
    if nb_ws_connections == 0:
        nb_ws_connections += 1
        while nb_ws_connections > 0:
            emit('info',
                    {
                        'status': status.get_information(),
                        'front': detect.get_front_distance(),
                        'left': detect.get_left_distance(),
                        'right': detect.get_right_distance(),
                        'back': detect.get_back_distance()
                    },
                    broadcast=True
            )
            time.sleep(5)
    else:
        nb_ws_connections += 1

@socketio.on('disconnect')
def socket_leave():
    print("client disconnected")
    global nb_ws_connections
    nb_ws_connections -= 1

@socketio.on('move')
def socket_move(message):
    make_move(message.speed, message.direction)

@socketio.on('stop')
def socket_stop(message):
    stop()
