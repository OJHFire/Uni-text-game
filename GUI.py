from tkinter import *

current_window = "menu"
render = None

window = Tk()
window.title("Welcome to the dungeon")

def draw():
    render = Canvas(window, width="1280", height="720")
    render.place(x=0,y=0)
    create_widgets()

def create_widgets():
    if current_window == "menu":
        Label(render, text="Welcome to the dungeon!!", font=("arial",32)).place(x=10,y=30)
        Button(render, text="Play", font=("arial", 32), bg="#99d6ff", command=menuToPlay()).place(x=10,y=100)
        Button(render, text="Settings", font=("arial", 32), bg="#adebad").place(x=10,y=200)
        Button(render, text="Scores", font=("arial", 32), bg="#b3b3ff").place(x=10,y=300)
        Button(render, text="Quit", font=("arial", 32), bg="#ff9999", command=window.destroy).place(x=10,y=400)
    elif current_window == "play":
        Label(render, text="Welcome to the dungeon!!", font=("arial", 32)).place(x=10,y=30)

def menuToPlay():
    pass
#     render.destroy
#     current_window = "play"
#     draw()

window.geometry("1280x720")
draw()
window.mainloop()