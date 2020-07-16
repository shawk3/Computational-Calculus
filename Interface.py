# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 10 14:23:21 2020

# @author: shawk
# """

# from tkinter import *
#from tkinter.ttk import *

import matplotlib
matplotlib.use("TkAgg")

# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk 
from functools import partial 

from Calc import Calc
from plots import FunctionPlots as fplt
import numpy as np


def Plot(a, b, f):
    a = float(a.get())
    b = float(b.get())
    f(a, b)
    return

# def Plotfp(a, b):
#     a = float(a.get())
#     b = float(b.get())
#     p.plotfp(a, b)
#     return

def updateCalcFunction(event):
    s = event.widget.get()
    def f(x):
        return eval(s)
    c.f = f
    
def clear():
    p.clearPlot()
    
def bisection(resultlabel, a, b):
    a = float(a.get())
    b = float(b.get())
    result = c.bisection(a,b)
    resultlabel.config(text = "root: " + str(result))
    
def newton(resultlabel, x):
    x = float(x.get())
    result = c.newton(x)
    resultlabel.config(text = "root: " + str(result))


root = tk.Tk()
root.geometry('250x370+100+200')
c = Calc(lambda x: x)
p = fplt(c)

flabel = tk.Label(root, text = "Enter function")
fentry = tk.Entry(root)
fentry.bind("<FocusOut>", updateCalcFunction)
# fentry.bind("<Enter>", updateCalcFunction)

x1 = tk.StringVar()  
x2 = tk.StringVar() 
x1entry = tk.Entry(root, textvariable = x1, width = 10)
x2entry = tk.Entry(root, textvariable = x2, width = 10)
Plotf = partial(Plot, x1, x2, p.plotf)
fbutton = tk.Button(root, text = "plot", command = Plotf)
Plotfp = partial(Plot, x1, x2, p.plotfp)
fpbutton = tk.Button(root, text = "plot derivative", command = Plotfp)
PlotInt = partial(Plot, x1, x2, p.plotInt)
intbutton = tk.Button(root, text = "plot integral", command = PlotInt)
clearbutton = tk.Button(root, text = "Clear", command = clear)
a = tk.StringVar()
b = tk.StringVar()
aentry = tk.Entry(root, textvariable = a, width = 10)
bentry = tk.Entry(root, textvariable = b, width = 10)
brootlabel = tk.Label(root, text = "root: ")
bisect = partial(bisection, brootlabel, a, b)
bisectbutton = tk.Button(root, text = "Run", command = bisect)
x = tk.StringVar()
xentry = tk.Entry(root, textvariable = x, width = 10)
nrootlabel = tk.Label(root, text = "root: ")
newt = partial(newton, nrootlabel, x)
newtbutton = tk.Button(root, text = "Run", command = newt)





# bisectbutton = tk.Button(root, text = B)


flabel.place(x = 5, y = 5)
fentry.place(x = 100, y = 5)
tk.Label(root, text = "Xmin").place(x = 5, y = 45)
x1entry.place(x = 45, y = 45)
x2entry.place(x = 45, y = 65)
tk.Label(root, text = "Xmax").place(x = 5, y = 65)
fbutton.place(x = 180, y = 50)
fpbutton.place(x = 10, y = 100)
intbutton.place(x = 10, y = 130)
clearbutton.place(x=180, y = 115)
tk.Label(root, text = "Bisection Method: ").place(x = 10, y = 175)
tk.Label(root, text = "Left Bound: ").place(x = 5, y = 200)
tk.Label(root, text = "Right Bound: ").place(x = 5, y = 220)
aentry.place(x = 85, y = 200)
bentry.place(x = 85, y = 220)
bisectbutton.place(x = 180, y = 210)
brootlabel.place(x = 20, y = 245)
tk.Label(root, text = "Newton's Method:").place(x=10, y = 280)
tk.Label(root, text = "Initial Guess: ").place(x = 5, y = 305)
xentry.place(x = 85, y = 305)
newtbutton.place(x = 180, y = 305)
nrootlabel.place(x = 20, y = 330)






root.mainloop()









