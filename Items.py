import datetime
from Items.py import Items
from User.py import foodly_user
class Items:
    def __init__(self, ItemID, User: foodly_user, Quantity, Price, ExpiryDate):
        ItemID=ItemID
        ItemName=ItemName
        User=User
        Quantity=Quantity
        Price=Price
        ExpiryDate=ExpiryDate

    def add_items(self, ItemName, Quantity, Price, SpoilTime): # set spoiltime in days
        ItemName=ItemName
        Quantity=Quantity
        Price=Price
        ExpiryDate=datetime.now() + timedelta(days=SpoilTime)
        
    def remove_items():
        pass
    def edit_items():
        pass
    def view_items():
        pass
    def search_items():
        pass        
class Cart:
    def __init__(self, User: foodly_user, Items: Items):
        User=User
        Items=Items
    def add_to_cart():
        pass
    def remove_from_cart():
        pass
    def add_to_favorites():
        pass
    def remove_from_favorites():
        pass
    
    
