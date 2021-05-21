import Cat
from Boss import Boss


class Catala(Boss):
    def __init__(self):
        self.mana = 150

    def fight(self, cat: Cat.Cat):
        if cat.murmana > self.mana:
            return "Катала была повержена, забери свой приз и " \
                   "лавры победителя, но вскоре прийдет время и " \
                   "на свет появится новая Катала, сильнее предыдущей, продолжай тренировки!"
        else:
            return "ХаХа ты проиграл надо было лучше тренироваться!"
