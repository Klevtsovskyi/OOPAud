from MilitaryObject import MilitaryObject


class GeneralStaff(MilitaryObject):

    def __init__(self, name, generals, documents):
        super().__init__(name)
        self.generals = generals
        self.documents = documents

    def __str__(self):
        return (
            f"General Staff `{self.name}`: "
            f"{self.generals} generals and "
            f"{self.documents} documents"
        )

    def accept(self, spy):
        spy.visit_general_staff(self)
