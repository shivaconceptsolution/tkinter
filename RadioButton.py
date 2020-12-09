import tkinter as tk
root = tk.Tk()
root.geometry("300x250")
v1= tk.IntVar()
v2= tk.IntVar()

def showcourse():
    s=''
    if v1.get()==1:
      s = s + "Python"
    if v2.get()==1:
      s=  s + "Pearl"  
    lbl.config(text=s)
   
     
    
tk.Checkbutton(root, 
              text="Python",
              padx = 20, 
              variable=v1
              ).pack(anchor=tk.W)
tk.Checkbutton(root, 
              text="Perl",
              padx = 20, 
              variable=v2
              ).pack(anchor=tk.W)
tk.Button(root,text="click",command=showcourse).pack()
lbl=tk.Label(root)
lbl.pack()


root.mainloop()



