import Rpi.GPIO

class Door():
    pin = 0
    def __init__(self,pin):
        self.pin = pin
        print('Setup')
    def open(self):
        print('Open')
    def close(self):
        print('Close')