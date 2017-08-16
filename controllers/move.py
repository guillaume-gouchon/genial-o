import time
from board import raspi_robot_board
import detect as detect
import recognize as recognize
from multiprocessing import Value

auto_pilot = Value('i', 1)

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

def set_auto_pilot(is_auto_pilot):
    if (auto_pilot.value != is_auto_pilot):
        print("set auto pilot", is_auto_pilot)
        stop()

        with auto_pilot.get_lock():
            auto_pilot.value = is_auto_pilot

        if is_auto_pilot == 1:
            start_auto_pilot()

def start_auto_pilot():
    print("start auto pilot")
    go_forward()
    while auto_pilot.value == 1 and detect.get_front_distance() > 10:
        print("auto pilot ON: going forward...")
        time.sleep(1)

    if auto_pilot.value == 0:
        print("stop auto pilot")
    else:
        # GENIAL-O found an obstacle
        print("found obstacle, what is it?")
        recognize.guess()

        left = detect.get_left_distance()
        right = detect.get_right_distance()
        if left < 10 and right < 10:
            stop()
            go_backward()
            time.sleep(5)
            rotate_left()
        elif detect.get_left_distance() > detect.get_right_distance():
            rotate_left()
        else:
            rotate_right()

        time.sleep(2)

        # start again
        start_auto_pilot()
