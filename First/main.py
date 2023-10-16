from SmallHouse import SmallHouse
from Human import Human


def main():
    Human.default_info(Human)
    h1 = Human()
    h1.info()
    sh = SmallHouse(50000)
    h1.buy_house(sh)
    h1.earn_money(100000)
    h1.buy_house(sh)
    h1.info()


if __name__ == "__main__":
    main()
