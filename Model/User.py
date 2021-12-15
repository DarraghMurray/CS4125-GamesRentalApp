from Model.Cart import Cart

class User:
    
    def __init__(self, userid, username, password, email, usertype):
        self.__userid = userid
        self.__UserName = username
        self.__PassWord = password
        self.__Email = email
        self.__usertype = usertype
        self.__cart = Cart()

    #adds an item/game to users cart when they press add to cart on an items store page
    def add_to_cart(self, item):
        self.__cart.AddToCart(item)

    #changes usertype when user subscribes or cancels their subscription
    def change_account_type(self, usertype):
        self.__usertype = usertype

    #returns account type
    def get_account_type(self):
        return self.__usertype

