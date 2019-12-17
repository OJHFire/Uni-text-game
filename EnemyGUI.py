from tkinter import *
from random import randint

global window
window = None

def create_window():
    global window
    window = Tk()
    window.title = "Fight"
    

def make_widgets():
    render = Canvas(window, width="600", height="100", bg="#222222")
    render.pack()
    Button(render, text="Attack", font=("arial", 32)).place(x=0, y=10)
    Button(render, text="Block", font=("arail", 32)).place(x=170, y=10)
    Button(render, text="Item", font=("arial", 32)).place(x=325, y=10)
    Button(render, text="Run", font=("arial", 32), command=run).place(x=458, y=10)

def Block():

    return True

def run():
    run = None
    num = randint(0, 10)
    if num >= 5:
        run = False
    else:
        run = True
    if run:
        window.destroy()
        return True

create_window()
make_widgets()

if window != None:
    window.geometry("600x100")
    window.mainloop()