from typing import List
from Model.StoreItem import StoreItem

class GameBundle(StoreItem):

    def __init__(self):
        self._games: List[StoreItem] = []

    def add(self, storeitem: StoreItem) -> None:
        self._games.append(storeitem)
        storeitem.parent = self

    def remove(self, storeitem: StoreItem) -> None:
        self._children.remove(storeitem)
        storeitem.parent = None

    def is_composite(self) -> bool:
        return True
        
    def getName(self):
        names: List[str] = []
        for child in self._games:
            names.append(child.getName())
        return names

    def getPrice(self) -> float:
        total = 0
        for child in self._games:
            total += child.getPrice()
        return total
