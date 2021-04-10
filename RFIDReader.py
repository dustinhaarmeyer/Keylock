from mfrc522 import SimpleMFRC522
import time

reader = ""

class Reader():
    def __init__(self):
        global reader
        reader = SimpleMFRC522()
    def read(self):
        global reader
        return reader.read()
    print('a')

while True:
    r = Reader()
    print(r.read())
    time.sleep(0.1)