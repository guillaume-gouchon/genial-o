import time
from board import raspi_robot_board
import detect as detect
import recognize as recognize
from multiprocessing import Value
from threading import Lock, Thread

auto_pilot = Value('i', 1)

thread = None
thread_lock = Lock()

def go_forward(speed=1):
    print("go forward at speed", speed)
    raspi_robot_board.set_motors(speed, 0, speed, 0)

def rotate_right(speed=1):
    print("rotate right at speed", speed)
    raspi_robot_board.set_motors(speed, 0, speed, 1)

def rotate_left(speed=1):
    print("rotate left at speed", speed)
    raspi_robot_board.set_motors(speed, 1, speed, 0)

def go_backward(speed=1):
    print("go backward at speed", speed)
    raspi_robot_board.set_motors(speed, 1, speed, 1)

def stop():
    print("stop")
    raspi_robot_board.set_motors(0, 0, 0, 0)

def shoot():
    print("fire !")
    raspi_robot_board.set_oc1(1)
    time.sleep(0.5)
    raspi_robot_board.set_oc2(1)
    time.sleep(1)
    raspi_robot_board.set_oc2(0)
    raspi_robot_board.set_oc1(0)

def set_auto_pilot(is_auto_pilot):
    if (auto_pilot.value != is_auto_pilot):
        print("set auto pilot", is_auto_pilot)
        stop()

        with auto_pilot.get_lock():
            auto_pilot.value = is_auto_pilot

        if is_auto_pilot == 1:
            global thread
            with thread_lock:
                if thread is None:
                    thread = Thread(target=start_auto_pilot)
                    thread.start()

DISTANCE_THRESHOLD = 35 # in cm

def start_auto_pilot():
    print("start auto pilot")
    go_forward()
    while auto_pilot.value == 1 and detect.get_front_left_distance() > DISTANCE_THRESHOLD and detect.get_front_right_distance() > DISTANCE_THRESHOLD:
        print("auto pilot ON: going forward...")
        time.sleep(0.2)

    stop()

    if auto_pilot.value == 0:
        print("stop auto pilot")
    else:
        # GENIAL-O found an obstacle
        print("found obstacle, what is it?")
        recognize.guess()

        left = detect.get_left_distance()
        right = detect.get_right_distance()
        if left < DISTANCE_THRESHOLD and right < DISTANCE_THRESHOLD:
            go_backward()
            time.sleep(3)
            rotate_left()
        elif detect.get_left_distance() > detect.get_right_distance():
            rotate_left()
        else:
            rotate_right()

        time.sleep(1)

        # start again
        start_auto_pilot()
