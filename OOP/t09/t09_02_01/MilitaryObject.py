import abc


class MilitaryObject(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def accept(self, spy):
        pass
