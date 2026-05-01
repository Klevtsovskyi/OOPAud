from tkinter import *


def is_palindrome(s: str):
    s = "".join(s.split())
    return s == s[::-1]


def callback(event=None):
    value = entry.get()
    result = "" if is_palindrome(value) else "не "
    label["text"] = f"{value} - {result}паліндром"


root = Tk()
root.geometry("600x400")
root.title("Перевірка паліндрому")

# контейнер для центрування
frame = Frame(root)
frame.pack(expand=True)

label = Label(frame, font=("Arial", 20), text="Введіть рядок")
entry = Entry(frame, font=("Arial", 20), bg="green", fg="white", justify="center")
btn = Button(frame, font=("Arial", 20), text="Перевірити", command=callback)

root.bind("<Return>", callback)

label.pack(pady=10)
entry.pack(pady=10, ipadx=50, ipady=5)
btn.pack(pady=10)
entry.focus()

root.mainloop()
