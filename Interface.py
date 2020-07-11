# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 10 14:23:21 2020

# @author: shawk
# """

import tkinter as tk 

from Calc import Calc
from plots import FunctionPlots as fplt


def Plot():
    a = 1
    b = 3
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
c = Calc(lambda x: x)

flabel = tk.Label(root, text = "Enter function")
fentry = tk.Entry(root)
fentry.bind("<FocusOut>", updateCalcFunction)


fbutton = tk.Button(root, text = "plot", command = Plot)

flabel.place(x = 5, y = 5)
fentry.place(x = 100, y = 5)
tk.Label(root, text = "Xmin").place(x = 5, y = 45)
tk.Label(root, text = "Xmax").place(x = 5, y = 65)
fbutton.place(x = 120, y = 50)
# fentry.bind("<Enter>", updateCalcFunction)



root.mainloop()









