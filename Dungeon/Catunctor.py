import Cat
from Boss import Boss


class Catunctor(Boss):
    def __init__(self):
        self.mana = 50

    def fight(self, cat: Cat.Cat):
        if cat.murmana > self.mana:
            return "Котунктор был убит но это только начало!"
        else:
            return "ХаХа ты проиграл надо было лучше тренироваться!"
