import tkinter as tk

window = tk.Tk()
window.geometry("300x250")
window.title("Message Example")
s= "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(master=window,text=s)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

window.mainloop()
