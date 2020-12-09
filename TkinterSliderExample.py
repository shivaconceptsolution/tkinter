from tkinter import *

master = Tk()

def show_values():
    print (w1.get(), w2.get())

w1 = Scale(master, from_=0, to=42)
w1.pack()
w2 = Scale(master,from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
w2.pack()
Button(master, text='Show', command=show_values).pack()
mainloop()
