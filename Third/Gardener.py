class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self): # Поднимает состояние каждого томата из списка на +1
        print("Все томаты подросли")
        self._plant.grow_all()

    def harvest(self): # Если все томаты поспели, обнуляет список томатов
        if self._plant.all_are_ripe():
            print("Все томаты собраны!")
            self._plant.give_away_all()
        else:
            print("Не все томаты еще выросли!")

    def knowledge_base():
        print("Справочник по садовоству:\n....\nОшибка! Найдите в интернете.\n")
