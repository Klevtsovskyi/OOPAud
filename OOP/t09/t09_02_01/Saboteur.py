from GeneralStaff import GeneralStaff
from MilitaryBase import MilitaryBase
from Spy import Spy


class Saboteur(Spy):

    def __init__(self, name):
        super().__init__(name)
        self.info = ""

    def __str__(self):
        return f"Saboteur {self.name}. {self.info}"

    def visit_general_staff(self, general_staff: GeneralStaff):
        self.info = (
            f"Destroyed {general_staff.generals} generals and "
            f"{general_staff.documents} documents"
        )
        general_staff.generals = 0
        general_staff.documents = 0

    def visit_military_base(self, military_base: MilitaryBase):
        self.info = (
            f"Destroyed {military_base.soldiers} soldiers and "
            f"{military_base.tanks} tanks"
        )
        military_base.soldiers = 0
        military_base.tanks = 0
