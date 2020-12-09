import tkinter as tk
window = tk.Tk()
window.geometry("300x250")
window.title("Event Example")
txt = tk.Text(master=window,height=100,width=200)
txt.pack()
txt.insert(tk.END,"Welcome in TextWidget of Django")
window.mainloop()
