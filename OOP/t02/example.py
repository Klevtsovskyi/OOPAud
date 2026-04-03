from turtle import *
colormode(255)


if __name__ == '__main__':
    shape("turtle")


    pencolor("darkblue")
    fillcolor(255, 255, 0)
    begin_fill()
    for _ in range(4):
        forward(100)
        left(90)
    end_fill()
    
    width(5)
    up()
    setpos(-100, -100)
    down()
    circle(50, 180)

    mainloop()
