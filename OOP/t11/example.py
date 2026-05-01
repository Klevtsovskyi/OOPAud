from tkinter import *

root = Tk()

entry = Entry(root, font="Arial 24")
entry.grid(row=1, column=1, sticky=N)
label = Label(root, font="Arial 24", text="Hello!")
label.grid(row=2, column=2, sticky=E)
label.bind("<Button-1>", lambda event: print(f"you clicked me! {event}"))


def callback():
    value = entry.get()
    label["text"] = value


btn1 = Button(root, text="Hello!", font="Arial 24")
btn1.configure(command=callback)
btn1.grid(row=3, column=1)
entry.focus()

root.mainloop()
