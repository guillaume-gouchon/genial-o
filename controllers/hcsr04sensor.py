import RPi.GPIO as GPIO
import time


class HCSR04(object):

    TIMEOUT = 10000 # in number of iterations

    def __init__(self, trigger_pin, echo_pin):
        GPIO.setmode(GPIO.BCM)

        self.trigger_pin = trigger_pin
        GPIO.setup(self.trigger_pin, GPIO.OUT)

        self.echo_pin = echo_pin
        GPIO.setup(self.echo_pin, GPIO.IN)

    def _send_trigger_pulse(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.0001)
        GPIO.output(self.trigger_pin, False)

    def _wait_for_echo(self, value, timeout):
        count = TIMEOUT
        while GPIO.input(self.echo_pin) != value and count > 0:
            count -= 1

    def get_distance(self):
        self._send_trigger_pulse()
        # self._wait_for_echo(True)
        start = time.time()
        # self._wait_for_echo(False)
        finish = time.time()
        pulse_len = finish - start
        distance_cm = pulse_len / 0.000058
        return distance_cm
