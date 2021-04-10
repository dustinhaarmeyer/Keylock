#import RPi.GPIO
import time
from time import sleep
from Keypad import Keypad
from RFIDReader import Reader
from Database import Database
#from LED import LED
#from Door import Door


k = Keypad()                        #Keypad
r = Reader()                        #RFID Reader
db = Database()                     #Database (mysql Server)


db = Database("localhost","root","securePassword")
print(db.state())

print("Starting Loop!")
while True:
    while k.read() == None:
        sleep(0.2)
    token = k.read()
    print(token)

    if token == "*":                #RFID Code for known user
        tag = r.read()
        answer = db.check(tag, "User")
        print(answer)
        if answer == "known":
            print("User is known")
        elif answer == "Unknown":
            print("Not known! Please retry")