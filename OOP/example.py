from tkinter import *

root = Tk()

entry = Entry(root, font="Arial 24")
entry.pack()
label = Label(root, font="Arial 24", text="Hello!")
label.pack()

def callback():
    value = entry.get()
    label["text"] = value


btn1 = Button(root, text="Hello!", font="Arial 24", command=callback)
btn1.pack()


root.mainloop()
