import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see
from time import *

def main():
    # Main program block
    display.setLeftLed(0)
    display.setRightLed(0)
    display.printText('Je suis GENIAL-O', 1)

    while True:
        display.printText(detect.getFrontDistance(), 3)
        sleep(5)

if __name__ == '__main__':
   main()
