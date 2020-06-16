import sys
sys.modules["tkinter"] = __import__("tkinter")
from tkinter import*
from tkinter import ttk
import datetime 
import random
import tkinter.messagebox
root = tk ()
class inventory(Frame):
    def _init_(self,master)

    self.master = master
    
    
    self.master.title("inventory system")
    self.master.geometry("1350x750+0+0")
    self.master.configure(background="powder blue")
        
    btnrow1= Frame(root,bd=20, width=1350,height=700,relief=RIDGE)
    btnrow1.grid()

    leftframe= Frame(btnrow1,bd=10,width=750,height=600,padx=10,relief=RIDGE)
    leftframe.pack(side=LEFT)

    rightframe=Frame(btnrow1,bd=10,width=560,height=600,padx=10,relief=RIDGE)
      
    rightframe.pack(side=RIGHT)


if __name__ == "__main__":
    root =Tk()
    #application = inventory(root)
    root.mainloop()