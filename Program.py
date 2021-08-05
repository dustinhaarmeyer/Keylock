import RPi.GPIO as GPIO
import time
from time import sleep
from RFIDReader import Reader
#from Database import Database
from Database import Textfile, Textfile2
from pad4pi import rpi_gpio
#from LED import LED
from Door import Door
import flask
from flask import redirect, request
import multiprocessing
import random

GPIO.setwarnings(False)
KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]
ROW_PINS = [5, 6, 13, 19] # BCM numbering
COL_PINS = [12, 16, 20] # BCM numbering
codeLenght = 0
code = ""  # Delete * out of this for working version

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
r = Reader()                                                                        #RFID Reader
d = Door(26)    #Board: 37)
#db = Database("localhost", "securePassword", "root", "Keylock")                     #Database (mysql Server)
userC = Textfile("/home/pi/Desktop/Program/code.txt")       #/home/pi/RFID Keysave/code.txt"
keyC = Textfile2("/home/pi/Desktop/Program/KeyCode.txt")  #"/home/pi/RFID Keysave/KeyCode.txt"
f = open("/home/pi/Dektop/Program/log.txt", "w")
f.write("Log opened")

app = flask.Flask(__name__)
def API(conf):
    app.run(host='0.0.0.0',port='5000')

config = {"Something":"SomethingElese"}
api = multiprocessing.Process(target=API, args=(config))
@app.route('/form', methods=['GET', 'POST'])
def form():
    name = request.args.get('name')
    email = request.args.get('email')
    phoneNumber = request.args.get('phone')
    birthdate = request.args.get('birthdate')

    print(birthdate)
    print(name)
    print(phoneNumber)
    print(email)
    code = random.randint(1000,9999)
    # code = submit(name, birthdate, phoneNumber, email)
    return "Please save this code, you need it: " + str(code)

def foundKey(key):
    f.write("Keypad pressed. Key:" + key)
    global code
    global codeLenght
    print(key)
    code += key
    codeLenght += 1

d.close()
print("Starting Loop!")
api.start()
keypad.registerKeyPressHandler(foundKey)
while True:
    while code == "":
        #code = input()
        #print('No button pressed')
        codeLenght = codeLenght

    if code == "*":                #RFID Code for known user
        code = ""
        codeLenght = 0

        tag = r.read()
        CodeNum = str(tag)
        CodeNum = CodeNum.split(' ')[0]
        f.write("RFID Tag found: " + CodeNum)
        print("RFID Tag: " + str(CodeNum))
        userNum = userC.search(str(CodeNum))
        print("User Number: " + str(userNum))
        if userNum != 0:
            f.write("User " + CodeNum + " is known")
            d.open()
            code = ""
            while code == "":
                sleep(0.2)
            d.close()
        else:
            f.write("User " + CodeNum + " not known")
            print("Not known! Please retry")
        f.flush()
    else:
        code = ""