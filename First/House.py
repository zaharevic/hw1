class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    # Возвращает цену с учетом скидки
    def final_price(self, per_sent):
        return self._price * (1 - per_sent / 100)
