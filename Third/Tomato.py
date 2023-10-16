class Tomato:
    states = {0: "Пусто", 1: "Росток", 2:"Зеленые помидоры", 3:"Спелые помидоры"} #Словарь состояний томата

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self): #Функция меняющая состояние на 1 в случае если томат не поспаел
        if self._state < 3:
            self._state += 1

    def is_ripe(self): # Проверяет томат на спелость(если томат спелый возвращает True)
        if self._state == 3:
            return True
        else:
            return False
