from Gardener import Gardener
from TomatoBush import TomatoBush


def main():
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()


if __name__ == '__main__':
    main()
