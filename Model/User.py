from Model.Cart import Cart
from Model.CartInterface import CartInterface

class User:
    
    def __init__(self, userid, username, address, password, email):
        self.__userid = userid
        self.__UserName = username
        self.__address = address
        self.__creditCardInfo = ""
        self.__PassWord = password
        self.__Email = email
        self.__cart = Cart()

    def addToCart(self, item):
        self.__cart.AddToCart(item)
        return

