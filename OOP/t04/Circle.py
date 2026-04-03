from time import sleep

from Figure import Figure
from turtle import *


class Circle(Figure):

    def __init__(self, x, y, r, colour):
        super().__init__(x, y, colour)
        self.r = r

    def draw(self):
        up()
        goto(self.x, self.y - self.r)

        pensize(0)
        pencolor(self.colour)
        fillcolor(self.colour)
        begin_fill()
        down()
        circle(self.r)
        end_fill()

if __name__ == '__main__':
    speed(0)

    c = Circle(0, 0, 100, "#76a214")
    c.show()

    sleep(0.1)
    for _ in range(100):
        c.move(1, 0)

    mainloop()
