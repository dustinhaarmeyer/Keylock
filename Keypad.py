# This example is a hello world example
# for using a keypad with the Raspberry Pi

import RPi.GPIO as GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

class Keypad():
    def __init__(self):
        global L1
        global L2
        global L3
        global L4
        global C1
        global C2
        global C3
        global C4

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(L1, GPIO.OUT)
        GPIO.setup(L2, GPIO.OUT)
        GPIO.setup(L3, GPIO.OUT)
        GPIO.setup(L4, GPIO.OUT)

        GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def readLine(self, line, characters):
        global L1
        global L2
        global L3
        global L4
        global C1
        global C2
        global C3
        global C4

        GPIO.output(line, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            return characters[0]
        if(GPIO.input(C2) == 1):
            return characters[1]
        if(GPIO.input(C3) == 1):
            return characters[2]
        if(GPIO.input(C4) == 1):
            return characters[3]
        GPIO.output(line, GPIO.LOW)
    
    def read(self):
        global L1
        global L2
        global L3
        global L4
        global C1
        global C2
        global C3
        global C4

        line1 = self.readLine(L1, ["1","2","3","A"])
        line2 = self.readLine(L2, ["4","5","6","B"])
        line3 = self.readLine(L3, ["7","8","9","C"])
        line4 = self.readLine(L4, ["*","0","#","D"])

        if line1 != None:
            return line1
        elif line2 != None:
            return line2
        elif line3 != None:
            return line3
        elif line4 != None:
            return line4
        else:
            return None

    def waitFor(self, button):
        k = Keypad()
        while k.read() != str(button):
            time.sleep(0.1)
        return k.read()

k = Keypad()
print(k.read())
