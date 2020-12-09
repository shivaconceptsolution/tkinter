import tkinter as tk
def fun():
    lbl.config(text="hello world")
window = tk.Tk()
window.geometry("300x250")
window.title("Event Example")
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()
btn = tk.Button(master=frame,text="click",command=fun)
btn.pack()
lbl = tk.Label(master=frame)
lbl.pack()

window.mainloop()
