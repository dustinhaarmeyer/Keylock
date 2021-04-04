from mfrc522 import SimpleMFRC522
import time

reader = ""

class Reader():
    def __init__(self):
        reader = SimpleMFRC522()
    def read(self):
        return reader.read()
    print('a')

while True:
    r = Reader()
    r.read()
    time.sleep(0.1)