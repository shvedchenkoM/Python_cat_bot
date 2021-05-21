from Catada import Catada
from Catala import Catala
from Catunctor import Catunctor


class Dungeon:
    @staticmethod
    def get_dungeons():
        ...

    @staticmethod
    def start(dungeon, cat):
        if dungeon == "bronza":
            boss = Catunctor()
            return boss.fight(cat)
        elif dungeon == "serebro":
            boss = Catada()
            return boss.fight(cat)
        else:
            boss = Catala()
            return boss.fight(cat)
