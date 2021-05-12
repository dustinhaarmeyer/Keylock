import RPi.GPIO as GPIO
import time
from time import sleep
from RFIDReader import Reader
#from Database import Database
from Database import Textfile
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
#db = Database("localhost", "securePassword", "root", "Keylock")                     #Database (mysql Server)
users = Textfile("/home/pi/Desktop/Program/code.txt")
keys = Textfile("/home/pi/Desktop/Program/code.txt")

#print(db.state())

def foundKey(key):
    #print(key)
    code += key
    codeLenght += 1

print("Starting Loop!")
keypad.registerKeyPressHandler(foundKey)
while True:
    while code == "":
        #print('No button pressed')
        codeLenght = codeLenght

    if code == "*":                #RFID Code for known user
        code = ""
        codeLenght = 0


        if answer:
            print("User is known")
            #d.open()
            print('Door opened')
            #k.waitFor("A")
            #d.close
            print('Door closed')
        else:
            print("Not known! Please retry")
    else:
        code = ""