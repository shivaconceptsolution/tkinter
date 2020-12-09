import tkinter as tk
window = tk.Tk()
txt = tk.Label(text="welcome in tkinter")
txt.pack()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()
label1 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label1.pack()
window.mainloop()
