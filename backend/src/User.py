import uuid
import mysql
import postgres 

class FoodlyUser:
    def __init__(self, user_id, first_name, last_name, email, username, password):  
        self._user_id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._username = username
        self._password = password
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    

    def __str__(self):
        return f"UserID: {self._user_id}, Name: {self._first_name} {self._last_name}, Email: {self._email}, Username: {self._username}, Password: {self._password}"

    @classmethod
    def create_user(cls):
        user_id = str(1)
        first_name = input("What is your name? ")
        last_name = input("What is your last name? ")
        email = input("What is your email? ")
        username = input("What is your username? ")
        password = input("What is your password? ")
        return cls(user_id, first_name, last_name, email, username, password)




#Postgres start here 


user = FoodlyUser.create_user() # Creat instance of object FoodlyUser
postgres = postgres.Postgress()

# User Data format

userdb = {
    "UserID": str(uuid.uuid4()),
    "FirstName": user.first_name,
    "LastName": user.last_name,
    "Email": user.email,
    "UserName": user.username,
    "Password": user.password
}

postgres.connect()
postgres.execute(userdb)
#postgres.result_print()
postgres.close()




# MySQL start here and save the data
# Create a new user
#user = FoodlyUser.create_user()

## Create an instance of MySQLDB
#db = mysql.MySQLDB()
## Connect to the database
#db.connect()
## Insert user data
#db.insert_user(userdb)
## Disconnect from the database
#db.disconnect()

