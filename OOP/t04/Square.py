from Rectangle import Rectangle
from turtle import *


class Square(Rectangle):

    def __init__(self, x, y, a, colour):
        super().__init__(x, y, a, a, colour)


if __name__ == '__main__':
    r = Square(50, 50, 300, "#f38412")
    r.show()

    r.move(-200, 100)

    mainloop()
