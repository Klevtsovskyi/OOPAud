from MilitaryObject import MilitaryObject


class MilitaryBase(MilitaryObject):

    def __init__(self, name, soldiers, tanks):
        super().__init__(name)
        self.soldiers = soldiers
        self.tanks = tanks

    def __str__(self):
        return (
            f"Military Base `{self.name}`: "
            f"{self.soldiers} soldiers and "
            f"{self.tanks} tanks"
        )

    def accept(self, spy):
        spy.visit_military_base(self)
