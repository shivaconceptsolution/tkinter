import tkinter as tk
from tkinter import messagebox as mb
window = tk.Tk()
window.geometry("300x250")
window.title("Event Example")
def answer():
    mb.showerror("Answer", "Sorry, no answer available") #alert box error

def callback():
    if mb.askyesno('Verify', 'Really quit?'):  #confirm box return true false
        mb.showwarning('Yes', 'Not yet implemented')  #alert box warning
    else:
        mb.showinfo('No', 'Quit has been cancelled')   #alert box info

tk.Button(text='Quit', command=callback).pack(fill=tk.X)
tk.Button(text='Answer', command=answer).pack(fill=tk.X)
tk.mainloop()
