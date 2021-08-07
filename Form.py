import random
from gsheets import sheet

class Form:
    loginNum = []
    def __init__(self):
        id_u= ""
        codeNumber = ""
        curr = 0
        self.gs = sheet('/Users/Ralf/Desktop/creds.json')
        with open('listfile.txt', 'r') as filehandle:
            for line in filehandle:
                currentPlace = line[:-1]
                if curr == 0:
                    id_u = currentPlace
                    curr = 1
                elif curr == 1:
                    codeNumber = currentPlace
                    curr = 0
                    x = unknownUser(id_u, codeNumber)
                    self.loginNum.append(x)

    def submit(self, name, email, phone, birthdate):
        if name != "" or email != "" or phone != "" or birthdate != "":
            num = random.randint(1111,9999)
            while self.check(num):
                num = random.randint(1111,9999)
            
            id_u = self.gs.addNewUnknown(name, email, phone, birthdate)
            self.addToFile(id_u, num)
            print("New unknown User with Code: " + str(num))
            return num
        else: return 0

    def check(self, num) -> int:
        for obj in self.loginNum:
            if str(num) == obj.codeNumber:
                return int(obj.id_u)
        return 0

    def addToFile(self, id_u, num):
        if id_u != "" and str(num) != "":
            self.loginNum.append(unknownUser(id_u, str(num)))
            # Add the Data to Google Sheet too
            print("Added User with Code: " + str(num))
            self.save()

    def save(self):
        with open('listfile.txt', 'w') as filehandle:
            for listitem in self.loginNum:
                filehandle.write('%s\n' % listitem.id_u)
                filehandle.write('%s\n' % listitem.codeNumber)
            filehandle.close()

class unknownUser:
    id_u = "" #id_u on Google Sheets 
    codeNumber = "" #Login Code
    def __init__(self, pid_u, pnum):
        self.id_u = str(pid_u)
        self.codeNumber = str(pnum)

