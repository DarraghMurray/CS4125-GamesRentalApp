
from Model.Price import Price
from Model.StoreItem import StoreItem


class Game(StoreItem):

    __releaseState = None
    
    def __init__(self, gameID, gameName, basePrice, rentalPrice, gameDescription, releaseState):
        self.__gameID = gameID
        self.__gameName = gameName
        self.__basePrice = basePrice
        self.__gameDescription = gameDescription
        self.transition_to(releaseState)

    def transition_to(self, releasestate: Price):
        self.__releaseState = releasestate
        self.__releaseState.context = self

    def getPrice(self) -> float:
        return self.__basePrice

    def getRentalPrice(self) -> float:
        return self.__releaseState.getPrice(self.__basePrice)

    def getName(self):
        return self.__gameName
    
    def getGameDescription(self):
        return self.__gameDescription

    def getGameID(self):
        return self.__gameID
