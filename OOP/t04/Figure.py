import abc


class Figure(metaclass=abc.ABCMeta):

    def __init__(self, x, y, colour="#000000"):
        self.x = x
        self.y = y
        self.colour = colour
        self.visible = False

    @abc.abstractmethod
    def draw(self):
        pass

    def show(self):
        self.visible = True
        self.draw()

    def hide(self):
        self.visible = False
        colour = self.colour
        self.colour = "#ffffff"
        self.draw()
        self.colour = colour

    def move(self, dx, dy):
        self.hide()
        self.x += dx
        self.y += dy
        self.show()

