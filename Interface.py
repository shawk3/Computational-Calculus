# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 10 14:23:21 2020

# @author: shawk
# """

import tkinter as tk 
from functools import partial 

from Calc import Calc
from plots import FunctionPlots as fplt


def Plot(a, b):
    a = float(a.get())
    b = float(b.get())
    p = fplt(c)
    N = 100
    p.plotf(a, b, N)
    return

def updateCalcFunction(event):
    s = event.widget.get()
    def f(x):
        return eval(s)
    c.f = f


root = tk.Tk()
root.geometry('300x200+100+200')
c = Calc(lambda x: x)

flabel = tk.Label(root, text = "Enter function")
fentry = tk.Entry(root)
fentry.bind("<FocusOut>", updateCalcFunction)
# fentry.bind("<Enter>", updateCalcFunction)

a = tk.StringVar()  
b = tk.StringVar() 
aentry = tk.Entry(root, textvariable = a)
bentry = tk.Entry(root, textvariable = b)
Plot = partial(Plot, a, b)
fbutton = tk.Button(root, text = "plot", command = Plot)


flabel.place(x = 5, y = 5)
fentry.place(x = 100, y = 5)
tk.Label(root, text = "Xmin").place(x = 5, y = 45)
aentry.place(x = 45, y = 45)
bentry.place(x = 45, y = 65)
tk.Label(root, text = "Xmax").place(x = 5, y = 65)
fbutton.place(x = 180, y = 50)




root.mainloop()









