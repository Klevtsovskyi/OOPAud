import abc

from GeneralStaff import GeneralStaff
from MilitaryBase import MilitaryBase


class Spy(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def visit_general_staff(self, general_staff: GeneralStaff):
        pass

    @abc.abstractmethod
    def visit_military_base(self, military_base: MilitaryBase):
        pass
