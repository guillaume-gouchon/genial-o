import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see
import time

def main():
    # Main program block
    display.setLeftLed(0)
    display.setRightLed(0)
    display.printText('Je suis GENIAL-O', 1)

    while True:
        display.printText(detect.getFrontDistance(), 3)
        time.sleep(5)

    see.startCamera()

if __name__ == '__main__':
   main()
