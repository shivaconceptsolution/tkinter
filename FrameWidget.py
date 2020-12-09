import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="Welcome in SCS", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="We provide training on Java,.NET,PHP,ios and Android", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()
