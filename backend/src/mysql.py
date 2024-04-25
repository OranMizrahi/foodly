import MySQLdb
import uuid

class MySQLDB:
    def __init__(self, host="localhost", port=3307, user="root", passwd="123123", db="foodly"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.db_connection = None
        self.cursor = None
    
    def connect(self):
        self.db_connection = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
        self.cursor = self.db_connection.cursor()
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.db_connection:
            self.db_connection.close()
    
    def insert_user(self, user_data):
        sql = "INSERT INTO foodly_user(UserID, FirstName, LastName, Email, UserName, Password) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (user_data["UserID"], user_data["FirstName"], user_data["LastName"], user_data["Email"], user_data["UserName"], user_data["Password"]))
        self.db_connection.commit()
