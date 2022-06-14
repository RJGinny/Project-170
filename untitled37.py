#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:33:31 2022

@author: riddhiekajain
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("600x600")
grade3label= Label(root)
grade4label=Label(root)
grade5label=Label(root)

class Grade3():
    
    def __init__(self, arts, maths):
        self.arts=arts
        self.maths=maths
        
    def percentage(self):
        total=self.arts+self.maths
        totalwith100=total*100
        grade3percentage=totalwith100/200
        grade3label["text"]=grade3percentage
        
class Grade4():
    
    def __init__(self, arts, maths):
        self.arts=arts
        self.maths=maths
        
    def percentage(self):
        total=self.arts+self.maths
        totalwith100=total*100
        grade4percentage=totalwith100/200
        grade4label["text"]=grade4percentage
        
class Grade5():
    
    def __init__(self, arts, maths):
        self.arts=arts
        self.maths=maths
        
    def percentage(self):
        total=self.arts+self.maths
        totalwith100=total*100
        grade5percentage=totalwith100/200
        grade5label["text"]=grade5percentage
        
objgrade3=Grade3(87, 66)
grade3btn=Button(root, text="CLICK HERE TO SEE GRADE 3", command=objgrade3.percentage)
grade3btn.pack(padx=20, pady=20)
grade3label.pack(padx=20, pady=20)

objgrade4=Grade4(54, 11)
grade4btn=Button(root, text="CLICK HERE TO SEE GRADE 4", command=objgrade4.percentage)
grade4btn.pack(padx=20, pady=20)
grade4label.pack(padx=20, pady=20)

objgrade5=Grade5(33, 15)
grade5btn=Button(root, text="CLICK HERE TO SEE GRADE 5", command=objgrade5.percentage)
grade5btn.pack(padx=20, pady=20)
grade5label.pack(padx=20, pady=20)
root.mainloop()