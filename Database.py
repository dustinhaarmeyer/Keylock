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
    def execute(self, command):
        self.cursor = self.Mdb.cursor()
        self.cursor.execute(command)

db = Database("localhost", "securePassword", "root", "Keylock")
print(db.state())