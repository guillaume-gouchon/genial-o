import os
import urllib2
import threading
import time

# import display as display


class CheckInternet(object):

    def __init__(self, interval=10):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.is_connected = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Method that runs forever """
        while True:
            try:
                urllib2.urlopen("http://www.google.com").close()
            except urllib2.URLError:
                print("Not Connected")
                if self.is_connected:
                    self.is_connected = False
                    display.print_text("NO INTERNET", 4)
            else:
                print("Connected")
                if not self.is_connected:
                    self.is_connected = True
                    display.print_text("CONNECTED", 4)

            time.sleep(self.interval)


class CheckHardware(object):

    def __init__(self, interval=10):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.is_connected = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Method that runs forever """
        while True:
            cpu_temperature = os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n","")

            p = os.popen('free')
            i = 0
            while 1:
                i = i + 1
                line = p.readline()
                if i==2:
                    ram = line.split()[1:4]
                    used_ram = 100 * ram[1] / ram[0]

            used_cpu = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
        ))

            print("temperature= {}C, ram usage={}%, cpu usage={}%".format(cpu_temperature, used_ram, used_cpu))
            display.print_text("{}C - RAM {}% - CPU {}%".format(cpu_temperature, used_ram, used_cpu), 3)

            time.sleep(self.interval)
