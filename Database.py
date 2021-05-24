# root = securePassword
#python -m pip install mysql-connector-python
import mysql.connector as mysql

class Database():
    succesfullyConnected = False
    Mdb = ""
    cursor = ""
    def __init__(self, host, dbp, dbu, dtb):
        try:
            print('Setup')
            self.Mdb = mysql.connect(host=host, user=dbu, password=dbp, database=dtb)
            #print("Connected Succesfully")
            self.succesfullyConnected = True
        except:
            self.succesfullyConnected = False
    def state(self):
        return self.succesfullyConnected
    def check(self, code):
        search = "SELECT * FROM Users WHERE code = '" + code + "'"
        self.execute(search)
        a = self.cursor.fetchall()
        print(a)
        #def insertKUser(self, code):
        #   sql = "INSER INTO Users"
        return "known"
    def execute(self, command):
        self.cursor = self.Mdb.cursor()
        self.cursor.execute(command)

class Textfile():
    codes = []
    f = ""
    def __init__(self,filename):
        self.f = open(filename, "r")
        for rows in self.f:
            x = rows.split()[0]
            self.codes.append(str(x))
    def search(self, code):
        n = 1
        if str(code) in self.codes:
            return 1
        return 0

#Test:
#userC = Textfile("code.txt")
#tag = {}
#tag[0] = "648458285181 xx x asd 12"

#CodeNum = str(tag[0])
#CodeNum = CodeNum.split()[0]
#print("RFID Tag: " + str(CodeNum))
#userNum = userC.search(CodeNum)
#print("User Number: " + str(userNum))