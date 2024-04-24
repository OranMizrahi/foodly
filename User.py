import Items
class foodly_user:
    def __init__(self, UserID, FirstName, LastName, Email, UserName, Password):  
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.UserName = UserName
        self.Password = Password
        
    def __str__(self):
        return self.FirstName + " " + self.LastName + " " + self.Email + " " + self.UserName
    
    
user1 = foodly_user(
    FirstName="Oran",
    LastName="Mizrahi",
    Email="oranmz@gmail.com",
    UserName="oranmz",
    Password="123123"
)