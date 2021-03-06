import pygsheets
import datetime
import time

class sheet:
    kUser = []
    keyList = []
    def __init__(self, file):
        gc = pygsheets.authorize(service_file=file)     	    #'/Users/Ralf/Desktop/creds.json'
        sh = gc.open('KeySave')
        self.keys = sh[0]
        self.kUsers = sh[1]
        self.unkUsers = sh[2]

        # Read Lists
        print("Starting Loading")
        self.readkUser()
        self.readKeys()
        print("Loaded")
    def readkUser(self):
        i = 1
        value = self.kUsers.get_value("B" + str(i+1))
        while value != "":
            self.kUser.append(value)
            i += 1
            value = self.kUsers.get_value("B" + str(i+1))
        
    def readKeys(self):
        i = 1
        value = self.keys.get_value("B" + str(i+1))
        while value != "":
            self.keyList.append(value)
            i += 1
            value = self.keys.get_value("B" + str(i+1))

    def takeKey(self, num, usertype, user):
        header = self.keys.cell("C" + str(int(num)+1))
        header.value = "taken"
        header.update()

        header = self.keys.cell("D" + str(int(num)+1))
        header.value = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        header.update()

        if usertype == "known" and str(user) != "0":
            header = self.kUsers.cell("C" + str(int(user) + 1))
            header.value = num
            header.update()

            header = self.keys.cell("F" + str(int(num) + 1))
            header.value = "K" + str(user)
            header.update()
        elif usertype == "unknown" and str(user) != "0":
            header = self.unkUsers.cell("E" + str(int(user) + 1))
            header.value = num
            header.update()
            
            header = self.keys.cell("F" + str(int(num) + 1))
            header.value = "U" + str(user)
            header.update()

    def returnKey(self, num, usertype, user):
        header = self.keys.cell("C" + str(int(num)+1))
        header.value = "returned"
        header.update()

        header = self.keys.cell("E" + str(int(num)+1))  #Cell: Last returned
        header.value = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        header.update()

        if usertype == "known" and str(user) != "0":
            header = self.kUsers.cell("C" + str(int(user) + 1))
            header.value = " "
            header.update()

            header = self.keys.cell("F" + str(int(user) + 1))
            header.value = " "
            header.update()
        elif usertype == "unknown" and str(user) != "0":
            header = self.unkUsers.cell("E" + str(int(user) + 1))
            header.value = " "
            header.update()
            
            header = self.keys.cell("F" + str(int(num) + 1))
            header.value = " "
            header.update()

    def findkUser(self, code):
        n = 0
        for x in self.kUser:
            n += 1
            if str(x) == str(code):
                return n
        return 0

    def findKeyTag(self, code):
        n = 0
        for x in self.keyList:
            n += 1
            if str(x) == str(code):
                return n
        return 0

    def findUserTaken(self, num):
        return str(self.keys.get_value("F" + str(int(num) + 1)))
        
    def hasKey(self, usertype, user):
        if usertype == "known" and str(user) != "0":
            value = self.kUsers.get_value("C" + str(int(user) + 1))
            if value != " " and value != "":
                return True 
            return False
        elif usertype == "unknown" and str(user) != "0":
            value = self.unkUsers.get_value("E" + str(int(user) + 1))
            if value != " " and value != "":
                return True 
            return False

    def addNewUnknown(self, name, email, phone):
        n = 2
        value = self.unkUsers.get_value("A" + str(n))
        while value != "":
            n += 1
            value = self.unkUsers.get_value("A" + str(n))
        
        header = self.unkUsers.cell("A" + str(n))  
        header.value = n - 1
        header.update()
        header = self.unkUsers.cell("B" + str(n))  
        header.value = name
        header.update()
        header = self.unkUsers.cell("C" + str(n))  
        header.value = email
        header.update()
        header = self.unkUsers.cell("D" + str(n))  
        header.value = phone
        header.update()
        return str(n-1)

#gs = sheet('/Users/Ralf/Desktop/creds.json')
#gs.addNewUnknown("name","email","phone")
#gs.returnKey(8, "unknown", 1)