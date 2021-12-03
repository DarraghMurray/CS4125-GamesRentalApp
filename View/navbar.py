import tkinter as tk

class navbar(tk.Frame):
    def __init__(self, master,controller):
        tk.Frame.__init__(self, master, bg="dark gray",width=100,height=master.winfo_screenheight())
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        self.buttonReg = tk.Button(self, text="register", command=self.goToRegister, borderwidth="0",fg="white", bg="dark gray")
        self.buttonLogIn = tk.Button(self, text="log-in", command=self.goToSignIn, borderwidth="0",fg="white", bg="dark gray")
        self.buttonStore = tk.Button(self, text="Store", command=self.goToStore, borderwidth="0",fg="white", bg="dark gray")
        self.buttonLibrary = tk.Button(self, text="Games Library", command=self.goToLibrary, borderwidth="0",fg="white", bg="dark gray")
        self.buttonSettings = tk.Button(self, text="User Settings",command=self.goToCart, borderwidth="0",fg="white", bg="dark gray")

        self.buttonReg.grid()
        self.buttonLogIn.grid()
        self.buttonStore.grid()
        self.buttonLibrary.grid()
        self.buttonSettings.grid()

    def goToRegister(self):
        self.controller.navigateToRegistration()
    
    def goToSignIn(self):
        self.controller.navigateToLogIn()

    def goToStore(self):
        self.controller.navigateToStore()

    def goToLibrary(self):
        self.controller.navigateToLibrary()

    def goToCart(self):
        self.controller.navigateToCart