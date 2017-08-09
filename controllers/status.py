from threading import Thread, Event
import psutil
import os
import urllib2
import time

import display as display


class CheckInternet(Thread):

    def __init__(self, interval=10):
        Thread.__init__(self)

        self.interval = interval
        self.is_connected = False

        self.daemon = True
        self.start()

    def run(self):
        while True:
            try:
                urllib2.urlopen("http://www.google.com").close()
            except urllib2.URLError:
                if self.is_connected:
                    print("Not Connected to Internet")
                    self.is_connected = False
                    display.print_text("NO INTERNET", 4)
            else:
                if not self.is_connected:
                    print("Connected to Internet")
                    self.is_connected = True
                    display.print_text("ONLINE", 4)

            time.sleep(self.interval)


class CheckHardware(Thread):

    def __init__(self, interval=10):
        Thread.__init__(self)

        self.interval = interval
        self.is_connected = False

        self.daemon = True
        self.start()

    def run(self):
        while True:
            cpu_temperature = os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n","")
            print("temperature= {}C".format(cpu_temperature))

            p = os.popen('free')
            i = 0
            while True:
                i += 1
                line = p.readline()
                if i == 2:
                    ram = line.split()[1:4]
                    used_ram = int(100 * float(ram[1]) / float(ram[0]))
                    print("ram usage= {}%".format(used_ram))

            used_cpu = psutil.cpu_percent(interval=1)
            print("cpu usage= {}%".format(used_cpu))

            display.print_text("{}C - RAM {}% - CPU {}%".format(cpu_temperature, used_ram, used_cpu), 3)

            time.sleep(self.interval)
