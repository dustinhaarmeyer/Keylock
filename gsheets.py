import pygsheets
import datetime
import time

class sheet:
    kUser = []
    unkUser = []
    def __init__(self, file):
        gc = pygsheets.authorize(service_file=file)     	    #'/Users/Ralf/Desktop/creds.json'
        sh = gc.open('KeySave')
        self.keys = sh[0]
        self.kUsers = sh[1]
        self.unkUsers = sh[2]
        self.readkUser()
        
    def readkUser(self):
        i = 1
        value = self.kUsers.get_value("B" + str(i+1))
        while value != "":
            self.kUser.append(value)
            i += 1
            value = self.kUsers.get_value("B" + str(i+1))

    def takeKey(self, num, usertype, user):
        header = self.keys.cell("B" + str(int(num)+1))
        header.value = "taken"
        header.update()

        header = self.keys.cell("C" + str(int(num)+1))
        header.value = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        header.update()

        if usertype == "known" and str(user) != "0":
            header = self.kUsers.cell("C" + str(int(user) + 1))
            header.value = num
            header.update()
        elif usertype == "unknown" and str(user) != "0":
            yx = ""

    def returnKey(self, num, usertype, user):
        header = self.keys.cell("B" + str(int(num)+1))
        header.value = "returned"
        header.update()

        header = self.keys.cell("D" + str(int(num)+1))
        header.value = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        header.update()

        if usertype == "known" and str(user) != "0":
            header = self.kUsers.cell("C" + str(int(user) + 1))
            header.value = " "
            header.update()
        elif usertype == "unknown" and str(user) != "0":
            yx = ""

    def findkUser(self, code):
        n = 0
        for x in self.kUser:
            n += 1
            if str(x) == str(code):
                return n
        return 0
        
    def hasKey(self, usertype, user):
        if usertype == "known" and str(user) != "0":
            value = self.kUsers.get_value("C" + str(int(user) + 1))
            if value != " " and value != "":
                return True 
            return False
        elif usertype == "unknown" and str(user) != "0":
            yx = ""

#gs = sheet('/Users/Ralf/Desktop/creds.json')