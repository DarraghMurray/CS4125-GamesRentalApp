import tkinter as tk

from View.ItemWidget import ItemWidget

# add a product name text box and view button that takes to game store page
class StoreItemWidget(ItemWidget):
    def __init__(self, parent, game):
        super.__init__(self, parent, game)
        self.viewGame = tk.Button(self, command=self.view_game)
        self.viewGame.pack(side="right")

    def view_game(self):
        pass
