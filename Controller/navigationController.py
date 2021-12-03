from View.LogInUI import LogInUI
from View.RegisterUI import RegisterUI
from View.ItemPageUI import ItemPageUI
from View.StoreUI import StoreUI

class NavigationController():

    def __init__(self, mainScreen):
        self.mainScreen = mainScreen
        
    def navigateToRegistration(self):
        self.mainScreen.setCurrentFrame(RegisterUI)

    def navigateToLogIn(self):
        self.mainScreen.setCurrentFrame(LogInUI)

    def navigateToStore(self):
        self.mainScreen.setCurrentFrame(StoreUI)

    def navigateToLibrary(self):
        self.mainScreen.setCurrentFrame(StoreUI)

    def navigateToCart(self):
        self.mainScreen.setCurrentFrame(StoreUI)