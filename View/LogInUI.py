
import tkinter as tk
from tkinter.constants import SOLID, W
from Controller.LogInController import LogInController
from View.RegisterUI import RegisterUI

class LogInUI(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.logInController = LogInController()
        self.font = ('Times', 14)
        self.grid()
        self.loadInterface()

    def loadInterface(self):
        self.loadLabels()
        self.loadEntries()
        self.loadButtons()

    def loadLabels(self):
        emailLabel = tk.Label(self,text="Enter Email", bg='#CCCCCC',font=self.font)
        passwordLabel = tk.Label(self,text="Enter Password", bg='#CCCCCC',font=self.font)

        emailLabel.grid(row=0, column=0, sticky=W, pady=10)
        passwordLabel.grid(row=1, column=0, pady=10)

    def loadEntries(self):
        self.email_tf = tk.Entry(master=self,font=self.font)
        self.pwd_tf = tk.Entry(master=self,font=self.font,show='*')
        
        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)

    def loadButtons(self):
        self.login_btn = tk.Button(master=self,width=15, text='Login', font=self.font, 
                            relief=SOLID,cursor='hand2',command=self.LogInBtn)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)

    def LogInBtn(self):
        self.logInController.LogIn(self.email_tf.get(), self.pwd_tf.get())
        self.master.switch_frame(RegisterUI)
    
    def destroy(self) -> None:
        return super().destroy()
