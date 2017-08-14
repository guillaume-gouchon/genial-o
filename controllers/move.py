import time
from board import raspi_robot_board
import detect as detect
from multiprocessing import Value

auto_pilot = Value('i', 1)

def go_forward(speed):
    print("go forward at speed", speed)
    raspi_robot_board.set_motors(speed, 0, speed, 0)

def rotate_right(speed):
    print("rotate right at speed", speed)
    raspi_robot_board.set_motors(speed, 0, speed, 1)

def rotate_left(speed):
    print("rotate left at speed", speed)
    raspi_robot_board.set_motors(speed, 1, speed, 0)

def go_backward(speed):
    print("go backward at speed", speed)
    raspi_robot_board.set_motors(speed, 1, speed, 1)

def stop():
    print("stop")
    raspi_robot_board.set_motors(0, 0, 0, 0)

def set_auto_pilot(is_auto_pilot):
    print("set auto pilot", is_auto_pilot)
    stop()
    old_value = auto_pilot.value

    with auto_pilot.get_lock():
        auto_pilot.value = is_auto_pilot

    if old_value == 0 and is_auto_pilot == 1:
        start_auto_pilot()

def start_auto_pilot():
    print("start auto pilot")
    while auto_pilot.value == 1:
        # TODO
        print("auto piloting...")
        time.sleep(3)
    print("stop auto pilot")
