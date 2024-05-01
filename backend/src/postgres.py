import psycopg2

class Postgress:
    def __init__(self, db_port=5435, db_name="testdb", db_user="testuser", db_password="123123"):
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
    
    def connect(self):
        self.db_connection = psycopg2.connect(
            port=self.db_port,
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        self.cursor = self.db_connection.cursor()


    def execute(self, user_data):
        sql = "INSERT INTO foodly_user(UserID, FirstName, LastName, Email, UserName, Password) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (user_data["UserID"], user_data["FirstName"], user_data["LastName"], user_data["Email"], user_data["UserName"], user_data["Password"]))
        self.db_connection.commit()
            
    def result_print(self):
        self.result = self.cursor.fetchone()
        print(f"PostgreSQL version: {result}")
        
    def close(self):
        self.cursor.close()
        self.db_connection.close()      
