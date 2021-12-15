import tkinter as tk
from Controller.navbarController import NavbarController

class MainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,bg="black",width=500,height=master.winfo_screenheight())
        self.navigator = NavbarController(self)
        self._frame = None
        self.navigator.navigate_to_login()

    def switch_frame(self,frame):
        new_frame = frame(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

    def goToLogIn(self):
        self.navigator.navigate_to_login()

    def goToRegister(self):
        self.navigator.navigate_to_registration()