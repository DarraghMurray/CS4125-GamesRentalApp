from Controller.UserControl import UserControl
from Controller.UserControl import UserControl
from Model.CartInterface import CartInterface

#manages individual store item page
class ItemPageController:

    def addToCart(item):
        CartInterface.AddToCart(item)

    def rentItem(item):
        pass
    