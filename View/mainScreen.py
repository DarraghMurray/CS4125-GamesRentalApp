import tkinter as tk
from View.LogInUI import LogInUI

class MainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,bg="black",width=500,height=master.winfo_screenheight())
        self._frame = None
        self.switch_frame(LogInUI)

    def switch_frame(self,frame):
        new_frame = frame(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame