from GeneralStaff import GeneralStaff
from OOP.t09.t09_02_01.MilitaryBase import MilitaryBase
from Spy import Spy


class SecretAgent(Spy):

    def __init__(self, name):
        super().__init__(name)
        self.info = ""

    def __str__(self):
        return f"Secret Agent {self.name}. {self.info}"

    def visit_general_staff(self, general_staff: GeneralStaff):
        documents = general_staff.documents
        general_staff.documents = 0
        self.info = str(general_staff) + f". Documents stolen: {documents}."

    def visit_military_base(self, military_base: MilitaryBase):
        self.info = str(military_base)
