from board import raspi_robot_board
import detect as detect

auto_pilot = 1

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
    auto_pilot = 1 if is_auto_pilot else 0
    if auto_pilot == 1:
        start_auto_pilot()

def start_auto_pilot:
    print("start auto pilot")
    while auto_pilot:
        # TODO
