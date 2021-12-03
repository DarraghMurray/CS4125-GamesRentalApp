import tkinter as tk

# add a product name text box and view button that takes to game store page
class StoreItemWidget(tk.Frame):
    def __init__(self, parent, game):
        tk.Frame.__init__(self, parent)

        self.game = game
        self.label = tk.Text(self, text=game.GetName(), anchor="w")

        self.button = tk.Button(self, command=self.goToITemPage)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="bottom", fill="x", padx=4)

    def get(self):
        pass

    def goToITemPage(self):
        #go to item page ui with specified game data
        pass