from Model.Price import Price, Prices


class NewReleaseRentalPrice(Price):

    def GetPrice(self, basePrice):
        return basePrice*Prices.NewRelease