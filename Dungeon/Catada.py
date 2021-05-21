import Cat
from Boss import Boss


class Catada(Boss):
    def __init__(self):
        self.mana = 100

    def fight(self, cat: Cat.Cat):
        if cat.murmana > self.mana:
            return "Катада убежала зализывать свои раны, ты можешь продолжать свой путь!"
        else:
            return "ХаХа ты проиграл надо было лучше тренироваться!"
