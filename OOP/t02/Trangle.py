from turtle import *


class Triangle:

    def __init__(self, x1, y1=None, x2=None, y2=None, x3=None, y3=None):
        if isinstance(x1, Triangle):
            self._p1 = x1._p1
            self._p2 = x1._p2
            self._p3 = x1._p3

            self._outline = x1._outline
            self._fill = x1._fill
            self._width = x1._width
        else:
            self._p1 = (x1, y1)
            self._p2 = (x2, y2)
            self._p3 = (x3, y3)

            self._outline = "#000000"
            self._fill = "#33baff"
            self._width = 3

    def __str__(self):
        return f"Triangle {self._p1} {self._p2} {self._p3} "

    def set_outline(self, colour):
        self._outline = colour

    def set_fill(self, colour):
        self._fill = colour

    def set_width(self, w):
        self._width = w

    def draw(self):
        up()
        goto(self._p1)
        fillcolor(self._fill)
        pencolor(self._outline)
        width(self._width)

        begin_fill()
        down()
        goto(self._p2)
        goto(self._p3)
        goto(self._p1)
        end_fill()


if __name__ == "__main__":
    speed(1)

    t = Triangle(33, -1, 100, 154, -40, 142)
    t2 = Triangle(t)
    t2.set_fill("#12a48b")
    # t.draw()
    # t2.draw()
    print(t)

    # mainloop()
