from rrb3 import *

import controllers.display
import controllers.detect
import controllers.move
import controllers.speak

BATTERY_VOLTAGE = 6 * 1.5
MOTOR_VOLTAGE = 6

global raspiRobotBoard = RRB3(BATTERY_VOLTAGE, MOTOR_VOLTAGE)



def main():
    # Main program block
    setLeftLed(1)
    print(getFrontDistance())
