import tkinter as tk
from tkinter.colorchooser import askcolor                  
s= "red"
def callback():
    global s
    result = askcolor(color="#6A9662", 
                      title = "Bernd's Colour Chooser")
    s=result[1]
    btn.config(fg=s)
    print(s)
    
root = tk.Tk()
btn=tk.Button(root, 
          text='Choose Color', 
          fg=s, 
          command=callback)
btn.pack(side=tk.LEFT, padx=10)
tk.Button(text='Quit', 
          command=root.quit,
          fg="red").pack(side=tk.LEFT, padx=10)
tk.mainloop()
