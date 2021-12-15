from Model.Price import Price,Prices

class OldReleaseRentalPrice(Price):

    def GetPrice(self, basePrice):
        return basePrice * Prices.OldRelease