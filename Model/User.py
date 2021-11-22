from Model.Cart import Cart
from Model.CartInterface import CartInterface

class User:
    
    def __init__(self, UserID, UserName, address, PassWord, Email):
        self.__UserID = UserID
        self.__UserName = UserName
        self.__address = address
        self.__creditCardInfo = ""
        self.__PassWord = PassWord
        self.__Email = Email
        self.__Cart = Cart()

    def addToCart(self, item):
        self.__Cart.AddToCart(item)
        return

