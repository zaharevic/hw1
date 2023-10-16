from Tomato import Tomato


class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i) for i in range(count)]

    def grow_all(self): [self.tomatoes[i].grow() for i in range(len(self.tomatoes))] #Все томаты из списка ростут

    def all_are_ripe(self): # Проверка на то, что все томаты поспаели
        for i in range(len(self.tomatoes)):
            if not self.tomatoes[i].is_ripe(): # Как только возращается False, выполение заканчивается
                return False
        return True

    def give_away_all(self): # "Обнуляет" список томатов
        self.tomatoes = []
