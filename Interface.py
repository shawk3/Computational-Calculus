# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 10 14:23:21 2020

# @author: shawk
# """


# # import tkinter
# from Calc import Calc
# from plots import FunctionPlots as plots

# import tkinter as tk  
# from functools import partial  
   
   
# def call_result(label_result, n1, n2):  
#     num1 = (n1.get())  
#     num2 = (n2.get())  
#     result = int(num1)+int(num2)  
#     label_result.config(text="Result = %d" % result)  
#     return  
   
# root = tk.Tk()  
# root.geometry('400x200+100+200')  
  
# root.title('Calculator')  
   
# number1 = tk.StringVar()  
# number2 = tk.StringVar()  
  
# labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)  
  
# labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)  
  
# labelResult = tk.Label(root)  
  
# labelResult.grid(row=7, column=2)  
  
# entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
# entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
# call_result = partial(call_result, labelResult, number1, number2)  
  
# buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)  
  
# root.mainloop() 

from tkinter import *
from tkinter.ttk import *
from functools import partial 
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Calc import Calc


def Plot(s, a, b):
    # plot.cla()
    s = s.get()
    def f(x):
        return eval(s)
    c = Calc(f)
    
    
    
    a = float(a.get())
    b = float(b.get())
    N = 100
    w = (b-a)/N
    # print(f)
    X = [a + w*i for i in range(N+1)]
    Y = [c.f(x) for x in X]
    plot.plot(X, Y)
    plot.set_xlim(a,b)
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan = 4)
    return

def Clear():
    plot.cla()
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan = 4)

root = Tk()



 
f = StringVar()
a = StringVar()
b = StringVar()
ef = Entry(root, textvariable=f).grid(row = 1, column = 0)
ea = Entry(root, textvariable=a).grid(row = 2, column = 0)
eb = Entry(root, textvariable=b).grid(row = 2, column = 1)
Plot = partial(Plot, f, a, b)

l = Label(root, text = "Enter function").grid(row = 0, column = 0)

b = Button(root, text = "plot", command = Plot).grid(row = 3, column = 0) 
b = Button(root, text = "clear", command = Clear).grid(row = 3, column = 1)


figure = Figure(figsize=(5, 4), dpi=100)
plot = figure.add_subplot(1, 1, 1)

# plot.plot(0.5, 0.3, color="red", marker="o", linestyle="")

# X = [ 0.1, 0.2, 0.3 ]
# Y = [ -0.1, -0.2, -0.3 ]
# plot.plot(X, Y, color="blue", marker="x", linestyle="")

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan = 4)



root.mainloop()









