import time
from multiprocessing import Process, Value

import server as server
import controllers.display as display
import controllers.detect as detect
import controllers.move as move
import controllers.speak as speak
import controllers.see as see
from controllers.status import *

def main():
    # main program block
    display.clear_text()
    display.set_left_led(0)
    display.set_right_led(0)
    display.print_text("Hello, I am GENIAL-O", 1)

    # display robot status
    CheckInternet()
    CheckHardware()

    while True:
        time.sleep(5)

if __name__ == "__main__":
    # start robot and server on different processes
    p = Process(target=main, args=())
    p.start()
    server.start()
    p.join()
