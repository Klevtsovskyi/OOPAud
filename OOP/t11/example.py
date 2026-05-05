from tkinter import *

root = Tk()

moving = False

canvas = Canvas(root, width=400, height=300)
canvas.pack()

oval = canvas.create_oval(150, 150, 200, 200, fill="red")


def moving_on(ev):
    global moving
    moving = True

def moving_off(ev):
    global moving
    moving = False


def move(ev):
    if moving:
        x = ev.x
        y = ev.y

        x0 = x - 25
        y0 = y - 25
        x1 = x + 25
        y1 = y + 25
        canvas.coords(oval, x0, y0, x1, y1)


def animate(ids):
    canvas.move(ids, 1, 0)
    canvas.after(10, animate, ids)

def animate_rect(ev):
    animate(rect)

rect = canvas.create_rectangle(100, 100, 150, 150, fill="blue")

canvas.tag_bind(rect, "<ButtonPress-1>", animate_rect)
canvas.tag_bind(oval, "<ButtonPress-1>", moving_on)
canvas.tag_bind(oval, "<ButtonRelease-1>", moving_off)
canvas.tag_bind(oval, "<Motion>", move)


root.mainloop()
