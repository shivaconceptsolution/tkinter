import tkinter as tk 
import mysql.connector 
from tkinter import *
mydb = mysql.connector.connect( 
  host = "localhost", 
  user = "root", 
  database = "php12batch"
)  
mycursor = mydb.cursor() 
sql = "INSERT INTO `student` (`rno`, `name`, `branch`, `fees`, `mobile`) VALUES (%s,%s,%s,%s,%s);"
val = ("1234", "xyz","CS","12000","981233444") 

mycursor.execute(sql, val) 
mydb.commit() 

print(mycursor.rowcount, "details inserted") 

# disconnecting from server 
mydb.close() 
