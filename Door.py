import RPi.GPIO as GPIO

class Door():
    pin = 0
    def __init__(self,pin):
        self.pin = pin
        print('Door Setup done')
    def open(self):
        GPIO.output(self.pin, 1)
        print('Door opened')
    def close(self):
        GPIO.output(self.pin, 0)
        print('Door closed')
