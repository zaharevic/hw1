from EngAlphabet import EngAlphabet


def main():
    ea = EngAlphabet()
    ea.print()
    print(ea.letters_num())
    print(ea.is_en_letter("F"))
    print(ea.is_en_letter("Щ"))
    ea.example()


if __name__ == "__main__":
    main()
