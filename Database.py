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

f = ""
class Textfile():
    def __init__(self,filename):
        global f
        f = open(filename, "r")
    def search(self, code):
        global f
        for x in f:
            if code in x:
                return True
        return False

file = Textfile("/home/pi/Desktop/Program/code.txt")

print(file.search("27264954481"))