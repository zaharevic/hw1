import string
from Alphabet import Alphabet


class EngAlphabet(Alphabet):
    def __init__(self):
        super(EngAlphabet, self).__init__("En", string.ascii_uppercase)

    # Возвращает количество букв в английском алфавите
    @staticmethod
    def __letters_num():
        return len(string.ascii_letters)//2

    # Проверяет отонстися ли буква к английскому алфавиту и возвращает ркзультат
    def is_en_letter(self, letter):
        if(letter in self.get_letters()):
            return True
        else:
            return False

    # Возвращает количество букв в алфавите (переписаный метод)
    def letters_num(self):
        return self.__letters_num()

    # Выводит текст на английском языке
    def example(self):
        print(f"Example text in english language")
