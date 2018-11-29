from tkinter import *


def run():
    window = Tk()
    window.title("TagCounter")

    window.geometry('550x200')

    lbl = Label(window, text="Hello")

    lbl.grid(column=0, row=0)

    btn = Button(window, text="Click")

    btn.grid(column=1, row=0)

    window.mainloop()


