from View.LogInUI import LogInUI
from View.RegisterUI import RegisterUI
from View.StoreUI import StoreUI
from View.LibraryUI import LibraryUI

class NavbarController():

    def __init__(self, mainscreen):
        self.main_screen = mainscreen
        
    def navigate_to_registration(self):
        self.main_screen.switch_frame(RegisterUI)

    def navigate_to_login(self):
        self.main_screen.switch_frame(LogInUI)

    def navigate_to_store(self):
        self.main_screen.switch_frame(StoreUI)

    def navigate_to_library(self):
        self.main_screen.switch_frame(LibraryUI)