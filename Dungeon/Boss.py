import abc
from abc import ABC
from Cat import Cat


class Boss(ABC):
    @abc.abstractmethod
    def fight(self, cat):
        pass
