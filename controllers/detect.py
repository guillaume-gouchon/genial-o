from board import raspi_robot_board
from hcsr04sensor import HCSR04

BACK_SENSOR_TRIGGER_PIN = 13
BACK_SENSOR_ECHO_PIN = 19
back_sensor = HCSR04(BACK_SENSOR_TRIGGER_PIN, BACK_SENSOR_ECHO_PIN)

LEFT_SENSOR_TRIGGER_PIN = 20
LEFT_SENSOR_ECHO_PIN = 21
left_sensor = HCSR04(LEFT_SENSOR_TRIGGER_PIN, LEFT_SENSOR_ECHO_PIN)

RIGHT_SENSOR_TRIGGER_PIN = 16
RIGHT_SENSOR_ECHO_PIN = 26
right_sensor = HCSR04(RIGHT_SENSOR_TRIGGER_PIN, RIGHT_SENSOR_ECHO_PIN)

def get_front_distance():
    distance = raspi_robot_board.get_distance()
    return distance

def _get_distance(sensor, name):
    distance = sensor.get_distance()
    return distance

def get_back_distance():
    return _get_distance(back_sensor, "back")

def get_left_distance():
    return _get_distance(left_sensor, "left")

def get_right_distance():
    return _get_distance(right_sensor, "right")
