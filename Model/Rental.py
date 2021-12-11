class Rental:
    def __init__(self, days_rented, item_rented):
        self.__DaysRented = days_rented
        self.__ItemRented = item_rented

    def getRentedGames(self):
        return self.__ItemRented