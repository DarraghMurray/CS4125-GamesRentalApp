from View.LogInUI import LogInUI
from View.RegisterUI import RegisterUI
from View.ItemPageUI import ItemPageUI
from View.StoreUI import StoreUI

class NavigationController():

    def __init__(self, mainscreen):
        self.mainScreen = mainscreen
        
    def navigateToRegistration(self):
        self.mainScreen.switch_frame(RegisterUI)

    def navigateToLogIn(self):
        self.mainScreen.switch_frame(LogInUI)

    def navigateToStore(self):
        self.mainScreen.switch_frame(StoreUI)

    def navigateToLibrary(self):
        self.mainScreen.switch_frame(StoreUI)

    def navigateToCart(self):
        self.mainScreen.switch_frame(StoreUI)