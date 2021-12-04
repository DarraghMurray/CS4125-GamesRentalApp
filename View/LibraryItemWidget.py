#make factory with store item widget?
import tkinter as tk
from View.ItemPageUI import ItemPageUI
from View.ItemWidget import ItemWidget

class LibraryItemWidget(ItemWidget):
    
    def __init__(self, parent, game) -> None:
        super.__init__()
        self.RunGame = tk.Button(self, command=self.launch_game)
        self.RunGame.pack(side="right")

    def launch_game(self):
        pass