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
        
    def plotf(self, a, b, N):
        f = self.c.f
        w = (b-a)/N
        X = [a + w*i for i in range(N+1)]
        Y = [f(x) for x in X]
        plt.plot(X,Y)
        
    def plotfp(self, a, b, N):
        f = self.c.fp
        w = (b-a)/N
        X = [a + w*i for i in range(N+1)]
        Y = [f(x) for x in X]
        plt.plot(X,Y)
        
if __name__ == '__main__':
    c = Calc(lambda x : x**2)
    p = FunctionPlots(c)
    p.plotf(-2, 2, 100)
    p.plotfp(-2, 2, 100)