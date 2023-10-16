class Alphabet:
    def __init__(self, lang, let):
        self.__lang = lang
        self.__letters = let

    # Выводит все буквы алфавита
    def print(self):
        print(self.__letters)

    # Возвращает количество букв алфаивта
    def letters_num(self):
        print(len(self.__letters))

    # Возвращает все буквы алфавита
    def get_letters(self):
        return self.__letters
