import RPi.GPIO as GPIO
import time
from time import sleep
from RFIDReader import Reader
from pad4pi import rpi_gpio
from Door import Door
from Form import Form, unknownUser
from gsheets import sheet
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
code = ""  # Add something to test the Different buttons

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
r = Reader()     #RFID Reader
fo = Form()
gs = sheet('/Users/Ralf/Desktop/creds.json')
d = Door(26)    #Board: 37)
f = open("/home/pi/Desktop/Program/log.txt", "w") #Log File
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
    f.write("API called by :" + name + ". Email:" + email + ", phone Number:" + phoneNumber + ", birthdate:" + birthdate + ".")
    print(birthdate)
    print(name)
    print(phoneNumber)
    print(email)
    num = fo.submit(name, email, phoneNumber, birthdate)
    return "Your 4-Digit Code to open the Door: " + str(num)

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
        codeLenght = codeLenght
        sleep(0.1)

    if code == "*":                #RFID Code for known user
        code = ""
        codeLenght = 0
        tag = r.read()
        CodeNum = str(tag)
        CodeNum = CodeNum.split(' ')[0]
        f.write("RFID Tag found: " + CodeNum)
        print("RFID Tag: " + str(CodeNum))
        userNum = gs.findkUser(CodeNum)  #userC.search(str(CodeNum))
        print("User Number: " + str(userNum))
        if userNum != 0:
            f.write("User is known. ID: " + userNum)
            if not gs.hasKey("known", userNum):
                d.open()
                code = ""
                while code == "":
                    sleep(0.2)
                d.close()
                code = ""
            else:
                f.write("User already has a Key!")
        else:
            f.write("User " + CodeNum + " not known")
            print("Not known! Please retry")
        f.flush()
    elif code == "0":   #Using the Code of the API
        code = ""
        print("Please enter your 4-Digit Code")
        while codeLenght < 4:
            sleep(0.1)
        print(code)
        #Check Code and Open the Door
    elif code == "#":   #Returning Key
        code = ""
        #Check Key and Open Door
    else:
        code = ""