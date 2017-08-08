from board import raspi_robot_board
from hcsr04sensor import sensor

BACK_SENSOR_TRIGGER_PIN = 38
BACK_SENSOR_ECHO_PIN = 40
back_sensor = sensor.Measurement(BACK_SENSOR_TRIGGER_PIN, BACK_SENSOR_ECHO_PIN)

LEFT_SENSOR_TRIGGER_PIN = 36
LEFT_SENSOR_ECHO_PIN = 37
left_sensor = sensor.Measurement(LEFT_SENSOR_TRIGGER_PIN, LEFT_SENSOR_ECHO_PIN)

RIGHT_SENSOR_TRIGGER_PIN = 33
RIGHT_SENSOR_ECHO_PIN = 35
right_sensor = sensor.Measurement(RIGHT_SENSOR_TRIGGER_PIN, RIGHT_SENSOR_ECHO_PIN)

def get_front_distance():
    distance = raspi_robot_board.get_distance()
    print("get front distance=", distance)
    return distance

def __get_distance(sensor, name):
    print("__get_distance", name)
    raw_measurement = sensor.raw_distance()
    metric_distance = sensor.distance_metric(raw_measurement)
    print("get", name, "distance=", metric_distance)
    return metric_distance

def get_back_distance():
    return __get_distance(back_sensor, "back")

def get_left_distance():
    return __get_distance(left_sensor, "left")

def get_right_distance():
    return __get_distance(right_sensor, "right")
