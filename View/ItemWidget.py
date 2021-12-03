from abc import ABC, abstractmethod
import tkinter as tk

class ItemWidget(ABC):
        def __init__(self, parent, game):

            self.game = game

            self.label = tk.Text(self, text=game.GetName(), anchor="w")
            self.button = tk.Button(self, command=self.goToITemPage)

            self.label.pack(side="top", fill="x")