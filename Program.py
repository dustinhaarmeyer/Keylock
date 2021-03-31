from Keypad import Keypad
import RPi.GPIO
import time
from time import sleep
from RFIDReader import Reader
from LED

k = Keypad()                        #Keypad
r = Reader()                        #RFID Reader
d = Door()                          #Keylock Door (Lock)
db = Database()                     #Database (mysql Server)
gLED = LED("16")                    #Green LED
rLED = LED("18")                    #Red LED

while True:
    while k.read() == None:
        sleep(0.2)
    token = k.read()
    print(token)
    #gLED.blink()

    if token == "*":                #RFID Code for known user
        tag = r.read()
        answer = db.check(tag, "User")
        #gLED.blink()
        #d.open()
    elif token == "#":              #Code for unknown User
        token = None
        while token3 == "":
            while token == None:    #token = Actual press
                k.read()            #token1 / 2 /3 = token already pressed
            #gLED.blink()
            if token1 == "":
                token1 = token      # Get the list of pressed tokens
            elif token2 == "":
                token2 = token
            elif token3 == "":
                token3 = token
            #gLED.blink()
            #gLED.blink()
        code = str(token1) + str(token2) + str(token3) + str(token4)
        print(code)
        #answer = db.check(code, "FormCode")
        if answer == True:          # Check the given code in the DB 
            d.open()
            k.waitFor("A")
            d.close()
        else:
            rLED.blink()
