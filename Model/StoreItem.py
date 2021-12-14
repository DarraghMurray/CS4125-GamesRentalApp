from abc import ABC, abstractmethod

class StoreItem(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, storeitem) -> None:
        #required as leaf of composite does not implement this method
        return

    def remove(self, storeitem) -> None:
        #required as leaf of composite does not implement this method
        return

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getPrice(self) -> float:
        pass