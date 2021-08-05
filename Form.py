import random

class Form:
    loginNum = []
    def __init__(self):
        name = ""
        email = ""
        phoneNumber = ""
        birthdate = ""
        codeNumber = ""
        curr = 0
        with open('listfile.txt', 'r') as filehandle:
            for line in filehandle:
                currentPlace = line[:-1]
                if curr == 0:
                    name = currentPlace
                    curr += 1
                elif curr == 1:
                    email = currentPlace
                    curr += 1
                elif curr == 2:
                    phoneNumber = currentPlace
                    curr += 1
                elif curr == 3:
                    birthdate = currentPlace
                    curr += 1
                elif curr == 4:
                    codeNumber = currentPlace
                    curr = 0
                    x = unknownUser(name, email, phoneNumber, birthdate, codeNumber)
                    self.loginNum.append(x)

    def check(self, num) -> bool:
        for obj in self.loginNum:
            if str(num) == obj.codeNumber:
                return True
        return False
    def submit(self, name, email, phone, birthdate):
        num = random.randint(1111,9999)
        while self.check(num):
            num = random.randint(1111,9999)
        self.loginNum.append(unknownUser(name, email, phone, birthdate, str(num)))
        print("Added User with Code: " + str(num))
        self.save()
        return num
    def save(self):
        with open('listfile.txt', 'w') as filehandle:
            for listitem in self.loginNum:
                filehandle.write('%s\n' % listitem.name)
                filehandle.write('%s\n' % listitem.email)
                filehandle.write('%s\n' % listitem.phoneNumber)
                filehandle.write('%s\n' % listitem.birthdate)
                filehandle.write('%s\n' % listitem.codeNumber)
                print(listitem.name)
            filehandle.close()

class unknownUser:
    name = ""
    email = ""
    phoneNumber = ""
    birthdate = ""
    codeNumber = ""
    def __init__(self, pname, pemail, pphoneNumber, pbirthdate, pnum):
        self.name = pname
        self.email = pemail
        self.phoneNumber = pphoneNumber
        self.birthdate = pbirthdate
        self.codeNumber = pnum