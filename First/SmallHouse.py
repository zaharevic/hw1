from House import House


class SmallHouse(House):
    def __init__(self, price):
        self._area = 40
        self._price = price
