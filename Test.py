import RPi.GPIO as GPIO
import time
from time import sleep
from Keypad import Keypad
from RFIDReader import Reader
from Database import Database
from pad4pi import rpi_gpio
#from LED import LED
#from Door import Door

KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]
ROW_PINS = [5, 6, 13, 19] # BCM numbering
COL_PINS = [12, 16, 20] # BCM numbering
codeLenght = 0
code = ""

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
r = Reader()                                                                        #RFID Reader
db = Database("localhost", "securePassword", "root", "Keylock")                     #Database (mysql Server)

print(db.state())

def printKey(key):
    print(key)
    code += key
    codeLenght += 1

print("Starting Loop!")
keypad.registerKeyPressHandler(printKey)
while True:
    while codeLenght <4:
        print('Code has 4 numbers!')

    if code == "*":                #RFID Code for known user
        tag = k.read()
        answer = db.check(tag, "User")
        print(answer)
        if answer == "known":
            print("User is known")
            #d.open()
            print('Door opened')
            #k.waitFor("A")
            #d.close
            print('Door closed')
        elif answer == "Unknown":
            print("Not known! Please retry")