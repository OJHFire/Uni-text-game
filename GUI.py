from tkinter import *

window = Tk()
window.title("The dungeon")

render = Canvas(window, width="1280", height="720", bg="#222222")
render.pack

def create_menu_canvas():
    global render
    render.destroy()
    render = Canvas(window, width="1280", height="720", bg="#222222")
    render.pack()

def create_inv_canvas():
    global render
    render.destroy()
    render = Canvas(window, wid="1280", height=300, bg="#222222")
    render.pack()

def menu():
    global render
    Button(render, text="Quit", font=("arial", 32), bg="grey", fg="white", command=window.destroy).place(x=10, y=230)
    Button(render, text="Play", font=("arial", 32), bg="grey", fg="white").place(x=10, y=30)
    Button(render, text="Scores", font=("arial", 32), bg="grey", fg="white").place(x=10, y=130)

def menuToInv(health, weapon, armour):
    global render
    Label(render, text="Inventory", font=("arial", 32)). place(x=0, y=0)
    Label(render, text="Health: " + health, font=("arial", 24)).place(x=10, y=130)

window.geometry("1280x720")
window.mainloop()