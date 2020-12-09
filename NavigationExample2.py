from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main  
# root window 
master.geometry("500x500") 
  
  
# function to open a new window  
# on a button click 
def login(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("400x400") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is a new window").pack() 


def reg():
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("400x400") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="Registration Form").pack() 
  
label = Label(master,  
              text ="This is the main window") 
  
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="Login",  
             command = login) 
btn.pack(pady = 10) 
btn = Button(master,  
             text ="Register",  
             command = reg) 
btn.pack(pady = 10) 
    
# mainloop, runs infinitely 
mainloop() 
