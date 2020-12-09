from tkinter import *
from PIL import Image, ImageTk
master = Tk() 
master.geometry("400x400") 
load = Image.open("1.jpg")
image = load.resize((450, 350), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(master, image=render)
#img.image = render
img.pack()

mainloop()
