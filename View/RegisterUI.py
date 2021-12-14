
import tkinter as tk
from tkinter import font
from tkinter.constants import SOLID, W
from Controller.RegisterController import RegisterController
from View.LogInUI import LogInUI

class RegisterUI(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.registerController = RegisterController()
        self.font = ('Times', 14)
        self.grid()
        self.loadInterface()

    def loadInterface(self):
        self.loadLabels()
        self.loadEntries()
        self.loadButtons()

    def loadLabels(self):
        emailLabel = tk.Label(master=self,text="Enter Email", bg='#CCCCCC',font=self.font)
        usernameLabel = tk.Label(master=self,text="Enter Username", bg='#CCCCCC',font=self.font)
        passwordLabel = tk.Label(master=self,text="Enter Password", bg='#CCCCCC',font=self.font)

        emailLabel.grid(row=0, column=0, sticky=W, pady=10)
        usernameLabel.grid(row=1,column=0,pady=10)
        passwordLabel.grid(row=2, column=0, pady=10)

    def loadEntries(self):
        self.email_tf = tk.Entry(master=self,font=self.font)
        self.username_tf = tk.Entry(master=self,font=self.font)
        self.pwd_tf = tk.Entry(master=self,font=self.font,show='*')
        
        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.username_tf.grid(row=1, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=2, column=1, pady=10, padx=20)

    def loadButtons(self):
        register_btn = tk.Button(master=self,width=15, text='Register', font=self.font, 
                            relief=SOLID,cursor='hand2',command=self.RegisterBtn)
        
        register_btn.grid(row=3, column=1, pady=10, padx=20)

    def RegisterBtn(self):
        self.registerController.Register(self.email_tf.get(), self.username_tf.get(),
         self.pwd_tf.get())
        self.master.switch_frame(LogInUI)
