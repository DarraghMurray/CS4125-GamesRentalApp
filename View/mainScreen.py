import tkinter as tk
from View.LogInUI import LogInUI

class mainScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,bg="black",width=500,height=master.winfo_screenheight())
        self.currentFrame = LogInUI
        self.previousFrame = self.currentFrame
        self.loadScreen()

    def setCurrentFrame(self, frame):
        self.previousFrame = self.currentFrame
        self.currentFrame.destroy(self)
        self.currentFrame = frame
        self.loadScreen()

    def loadScreen(self):
        self.currentFrame(self)
