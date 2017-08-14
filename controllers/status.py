from threading import Thread, Event
import psutil
import os
import urllib2
import time

import display as display

def get_information():
    response = []

    # get CPU temperature
    cpu_temperature = int(float(os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n","")))
    # print("temperature= {}C".format(cpu_temperature))
    response.append(cpu_temperature)

    # get CPU usage
    used_cpu = int(psutil.cpu_percent(interval=1))
    # print("cpu usage= {}%".format(used_cpu))
    response.append(used_cpu)

    # get RAM usage
    p = os.popen('free')
    for i in range(0, 2):
        line = p.readline()
    ram = line.split()[1:4]
    used_ram = int(100 * float(ram[1]) / float(ram[0]))
    # print("ram usage= {}%".format(used_ram))
    response.append(used_ram)

    return response


class CheckInternet(Thread):

    def __init__(self, interval=30):
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
                    # print("Connected to Internet")
                    self.is_connected = True
                    display.print_text("ONLINE", 4)

            time.sleep(self.interval)


class CheckHardware(Thread):

    def __init__(self, interval=30):
        Thread.__init__(self)

        self.interval = interval
        self.is_connected = False

        self.daemon = True
        self.start()

    def run(self):
        while True:
            info = get_information()
            display.print_text("{}\x01C CPU {}% RAM {}%".format(info[0], info[1], info[2]), 3)
            time.sleep(self.interval)
