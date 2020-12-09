import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=500, height=500, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame1 = tk.Frame(master=window, width=500, height=500, bg="green")
frame1.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()
