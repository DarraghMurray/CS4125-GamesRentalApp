from CartInterface import CartInterface


class Cart(CartInterface):
    def __init__(self):
        return

    def UpdateCart(self):
        pass

    def AddToCart(self, item):
        self.__itemNames.append(item)
        #query = "INSERT INTO cart(GameID, UserID) VALUES(%s,%s,%s)"
        #parameters = (item.getGameID())
        #DC.executeStatement(query, parameters)

    def RemoveFromCart(self, item):
        if item in self.__itemNames:
            self.__itemNames.remove(item)
    
    def ClearCart(self):
        self.__itemNames.clear()

    def CheckOut(self):
        #calls appropriate methods to begin transaction
        #on successful purchase add to database games library
        pass