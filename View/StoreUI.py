import tkinter as tk
from tkinter import ttk
from Controller.StoreController import StoreController

class StoreUI(tk.Frame):
    def __init__(self,master) -> None:
        tk.Frame.__init__(self,master)
        self.storeController = StoreController()

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)