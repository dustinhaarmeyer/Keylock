import Rpi.GPIO
from time import sleep

class LED():
    pin = 0
    def __init__(self, pin):
        self.pin = pin
        print('Setup')
    def on(self):
        print('On')
    def off(self):
        print('Off')
    def blink(self):
        self.pin
        print('blink')
        sleep(0.1)