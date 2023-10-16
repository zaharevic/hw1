class Human:
    # Константы (я надеюсь, что в пайтоне они помечаются так)
    __DEFAULT_NAME = "default"
    __DEFAULT_AGE = 0

    def __init__(self, name=__DEFAULT_NAME, age=__DEFAULT_AGE, money=0, house=[]):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    # Выводи информацию о человеке
    def info(self):
        print(f"name: {self.name}, age = {self.age}, money = {self.__money}, house = {self.__house}")

    # Выводит константы
    def default_info(self):
        print(f"default_name = {self.__DEFAULT_NAME}, default_age = {self.__DEFAULT_AGE}")

    # Уменьшает деньги(money) и добавляет дом(house) к человеку
    def __make_deal(self, coast, house):
        self.__money -= coast
        self.__house.append(house)

    # Добавляет money человеку
    def earn_money(self, earned):
        self.__money += earned
        print(f"Human заработал {earned} у.е.")

    # Функция покупки дома если достаточно денег, то сделка совершается, если нет выводит, что недостаточно денег
    def buy_house(self, house):
        if self.__money >= house.final_price(0):
            print("Сделка совершена")
            self.__make_deal(house.final_price(0), house)
        else:
            print("Ошибка! Недостаточно денег!")
