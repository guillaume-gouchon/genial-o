from time import *

import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see

def main():
    # Main program block
    display.clear_text()
    display.set_left_led(0)
    display.set_right_led(0)
    display.print_text("Hello", 1)
    display.print_text("Je suis GENIAL-O", 2)

    while True:
        display.print_text(detect.get_front_distance(), 3)
        # display.print_text(detect.get_back_distance(), 4)
        sleep(5)

if __name__ == "__main__":
   main()
