from tkinter import *
from baseapplication import app
import tkinter as tk


def run():
    root = Tk()
    root.title("Tags counter")


    # Add a grid
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=10, padx=10)

    # Create a Tkinter variable
    tkvar = StringVar(root)

    # Dictionary with options
    choices = app.store.getAllValues()
    tkvar.set('Please, select the site...')  # set the default option

    tagsBox = Text(mainframe,height=30, width=50)
    tagsBox.grid(row=4, column=1)


    urlBox = Text(mainframe,height=1,width=50)
    urlBox.grid(row=1, column=1)

    def optionMenu_SelectionEvent(event):
        insertToTextBox(urlBox, event)

    popupMenu = OptionMenu(mainframe, tkvar, *choices, command=optionMenu_SelectionEvent)
    popupMenu.grid(row=0, column=1)

    def getUrl():
        return urlBox.get(1.0, tk.END).rstrip("\n\r")

    def showAction():
        url = getUrl()
        tags = app.runView(url)
        if tags is None:
            insertToTextBox(tagsBox, "No data. Please, load...")

        tagsStr = list(tagsToString(tags))
        insertToTextBox(tagsBox, "".join(tagsStr))

    bShow = Button(mainframe, text="Show tags info", command=showAction)
    bShow.grid(row=2, column=1)

    def loadAction():
        url = getUrl()
        app.runGet(url)

    bLoad = Button(mainframe, text="Load tags info", command=loadAction)
    bLoad.grid(row=3, column=1)

    root.mainloop()


def insertToTextBox(textBox, text):
    textBox.delete(1.0, tk.END)
    textBox.insert(1.0, text)

def tagsToString(tags):
    for the_key, the_value in tags.items():
        yield str(the_key)
        yield ":"
        yield str(the_value)
        yield "\n"


