from time import *
import thread

import server as server
import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see

def main():
    # main program block
    display.clear_text()
    display.set_left_led(0)
    display.set_right_led(0)
    display.print_text("Hello", 1)
    display.print_text("Je suis GENIAL-O", 2)

def flaskThread():
    server.app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    # start server in another thread
    thread.start_new_thread(flaskThread, ())

    main()
