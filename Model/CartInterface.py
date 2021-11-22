import abc

class CartInterface(abc.ABC):
    
    def UpdateCart(self):
        pass

    def AddToCart(self, item):
        pass

    def RemoveFromCart(self,item):
        pass

    def ClearCart(self):
        pass