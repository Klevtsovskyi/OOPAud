from turtle import *
from Figure import Figure


class Rectangle(Figure):

    def __init__(self, x, y, a, b, colour):
        super().__init__(x, y, colour)
        self.a = a
        self.b = b

    def draw(self):
        up()
        goto(self.x, self.y)

        pensize(0)
        pencolor(self.colour)
        fillcolor(self.colour)
        begin_fill()
        down()
        setheading(0)
        for _ in range(2):
            forward(self.a)
            left(90)
            forward(self.b)
            left(90)
        end_fill()


if __name__ == '__main__':
    r = Rectangle(50, 50, 300, 200, "#f38412")
    r.show()

    r.move(-200, 100)

    mainloop()
