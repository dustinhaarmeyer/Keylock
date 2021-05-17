import RPi.GPIO as GPIO
from time import sleep

pin = 37

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, 1)
    print(1)
    sleep(1)
    GPIO.output(pin, 0)
    print(0)
    sleep(1)