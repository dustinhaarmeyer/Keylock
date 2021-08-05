import pygsheets
import datetime
import time

class sheet:
    keys = ""
    kUsers = ""
    unkUsers = ""
    def __init__(self):
        gc = pygsheets.authorize(service_file='/Users/Ralf/Desktop/creds.json')
        sh = gc.open('Keys')
        self.keys = sh[0]
        self.kUsers = sh[1]
        self.unkUsers = sh[2]
        
    def takeKey(self, num):
        header = self.keys.cell("B" + str(int(num)+1))
        header.value = "taken"
        header.update()

        header = self.keys.cell("C" + str(int(num)+1))
        header.value = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        header.update()

    def returnKey(self, num):
        header = self.keys.cell("B" + str(int(num)+1))
        header.value = "returned"
        header.update()

        header = self.keys.cell("D" + str(int(num)+1))
        header.value = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        header.update()

sh = sheet()
sh.takeKey(3)
sh.returnKey(1)