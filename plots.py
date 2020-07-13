# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:39:36 2020

@author: shawk
"""
import matplotlib.pyplot as plt
from Calc import Calc

class FunctionPlots:
    def __init__(self, c):
        self.c = c
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        
        
    def newPlot(self, f, a, b, N):
        w = (b-a)/N
        X = [a + w*i for i in range(N+1)]
        Y = [f(x) for x in X]
        self.ax.plot(X,Y)
        plt.show(block = False)
        
    def clearPlot(self):
        self.ax.cla()
        plt.show(block = False)
        
        
        
    def plotf(self, a, b, N = 100):
        f = self.c.f
        self.newPlot(f, a, b, N)
        
    def plotfp(self, a, b, N = 100):
        f = self.c.fp
        self.newPlot(f, a, b, N)
        
    def plotInt(self, a, b, N=100):
        def f(x):
            return self.c.trap(0,x,N)
        self.newPlot(f, a, b, N)
        
if __name__ == '__main__':
    c = Calc(lambda x : x**2)
    p = FunctionPlots(c)
    p.plotf(-2, 2, 100)
    p.plotfp(-2, 2, 100)
    p.plotInt(-2, 2)