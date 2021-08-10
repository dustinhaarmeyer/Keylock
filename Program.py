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
gs = sheet('/Users/Ralf/Desktop/creds.json')
fo = Form(gs)  #Let Form use the Google Sheet functions without Loading everything again
d = Door(26)    #Board: 37)
print("Log opened")

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
    print("API called by :" + name + ". Email:" + email + ", phone Number:" + phoneNumber +  ".")
    print(name)
    print(phoneNumber)
    print(email)
    num = fo.submit(name, email, phoneNumber)
    return "Your 4-Digit Code to open the Door: " + str(num)

def foundKey(key):
    print("Keypad pressed. Key:" + key)
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
        print("Start reading a Tag")
        tag = r.read()
        CodeNum = str(tag)
        CodeNum = CodeNum.split(' ')[0]
        print("RFID Tag: " + str(CodeNum))
        userNum = gs.findkUser(CodeNum)  #userC.search(str(CodeNum))
        print("User Number: " + str(userNum))
        if userNum != 0:
            print("User is known. ID: " + str(userNum))
            if not gs.hasKey("known", userNum):
                d.open()
                print("Waiting for Key RFID")
                tag = r.read()
                CodeNum = str(tag)
                CodeNum = CodeNum.split(' ')[0]
                print("RFID Tag found: " + str(CodeNum))
                KeyNum = gs.findKeyTag(CodeNum)
                if KeyNum == 0:     #  Find Error while Reading
                    print("Error while Reading. Please put the Tag attached to your Key again on the Scanner")
                    sleep(0.5)
                    tag = r.read()
                    CodeNum = str(tag)
                    CodeNum = CodeNum.split(' ')[0]
                    print("RFID Tag found: " + str(CodeNum))
                    KeyNum = gs.findKeyTag(CodeNum)
                    if KeyNum == 0:
                        print("Key cant be found. Admin will be Notificated!")
                        d.close()
                if KeyNum != 0:
                    gs.takeKey(KeyNum, "known", userNum)
            else:
                print("User already has a Key!")
        else:
            print("Card " + str(CodeNum) + " not known")
    elif code == "0":   #Using the Code of the API
        code = ""
        print("Please enter your 4-Digit Code")
        while codeLenght < 4:
            sleep(0.1)
        print(code)
        userNum = fo.check(code) 
        if userNum != 0:
            if gs.hasKey("unknown", userNum):
                d.open()
                print("Waiting for Key RFID")
                tag = r.read()
                CodeNum = str(tag)
                CodeNum = CodeNum.split(' ')[0]
                print("RFID Tag found: " + str(CodeNum))
                KeyNum = gs.findKeyTag(CodeNum)
                if KeyNum == 0:     #  Find Error while Reading
                    print("Error while Reading. Please put the Tag attached to your Key again on the Scanner")
                    sleep(0.5)
                    tag = r.read()
                    CodeNum = str(tag)
                    CodeNum = CodeNum.split(' ')[0]
                    print("RFID Tag found: " + str(CodeNum))
                    KeyNum = gs.findKeyTag(CodeNum)
                    if KeyNum == 0:
                        print("Key cant be found. Admin will be Notificated!")
                        d.close()
                if KeyNum != 0:
                    gs.takeKey(KeyNum, "unknown", userNum)
        else:
            print("Your 4-Digit Code cannot be found")
        #Check Code and Open the Door
    elif code == "#":   #Returning Key
        code = ""
        print("Please put the RFID Tag of the Key on the Scanner")
        tag = r.read()
        CodeNum = str(tag)
        CodeNum = CodeNum.split(' ')[0]
        print("RFID Tag found: " + str(CodeNum))
        KeyNum = gs.findKeyTag(CodeNum)
        if KeyNum == 0:
            print("Error while scanning the Tag, is it the Right one? Please retry!")
        else:
            d.open()
            print("Door opened")
            # Search User out of Key file
            user = gs.findUserTaken(KeyNum)
            if "K" in user:
                user = str(user.split("K", 1)[1])
                gs.returnKey(KeyNum, "known", user)
            elif "U" in user:
                user = str(user.split("U", 1)[1])
                gs.returnKey(KeyNum, "unknown", user)
            else: 
                print("Error: User Code is wrong!")
            code = ""
            print("Press any button to close the Door")
            while code == "":
                sleep(0.2)
            d.close()
            code = ""
    else:
        code = ""