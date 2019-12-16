from tkinter import *

window = Tk()
window.title("The dungeon")
render = Canvas(window, width="1280", height="720", bg="#222222")
render.pack()


Button(render, text="Quit", font=("arial", 32), bg="grey", fg="white", command=window.destroy).place(x=10, y=230)
Button(render, text="Play", font=("arial", 32), bg="grey", fg="white").place(x=10, y=30)
Button(render, text="Scores", font=("arial", 32), bg="grey", fg="white").place(x=10, y=130)

window.geometry("1280x720")
window.mainloop()