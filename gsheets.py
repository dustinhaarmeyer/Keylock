import pygsheets
import datetime
import time

class sheet:
    Kuser = []
    def __init__(self):
        gc = pygsheets.authorize(service_file='/Users/Ralf/Desktop/creds.json')
        sh = gc.open('KeySave')
        self.keys = sh[0]
        self.kUsers = sh[1]
        self.unkUsers = sh[2]
        self.readKUser()
        
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

    def readKUser(self):
        i = 1
        value = self.kUsers.get_value("B" + str(i+1))
        while value != "":
            self.Kuser.append(value)
            i += 1
            value = self.kUsers.get_value("B" + str(i+1))

    def findKUser(self,code):
        n = 0
        for x in self.Kuser:
            n += 1
            if str(x) == str(code):
                return n
        return 0
        

sh = sheet()
sh.takeKey(3)
sh.returnKey(1)

print(sh.findKUser(27264954481))