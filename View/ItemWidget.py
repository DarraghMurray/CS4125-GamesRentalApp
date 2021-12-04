from abc import ABC, abstractmethod
import tkinter as tk

class ItemWidget(ABC):
        def __init__(self, parent, game):
            self.game = game
            self.label = tk.Text(self, text=game.GetName(), anchor="w")
            self.label.pack(side="left", fill="x")