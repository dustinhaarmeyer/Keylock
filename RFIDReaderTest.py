from mfrc522 import SimpleMFRC522
import time

reader = ""

class Reader():
    def __init__(self):
        global reader
        reader = SimpleMFRC522()
    def read(self):
        global reader
        read = reader.read()
        if read == None or read == "":
            print('No code')
        return read
    
r = Reader()

while True:
    print (r.read())
    