# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:08:14 2020

@author: shawk
"""


class Calc():
    def __init__(self, f, tolerance = 0.0001):
        self.tol = tolerance
        self.f = f
        
    def bisection(self, a, b):
        f = self.f
        if f(a)*f(b) > 0:
            return "Invalid bounds"
        
        while abs(a-b) > self.tol:
            c = (a+b)/2
            if f(a)*f(c) > 0:
                a = c
            else:
                b = c
        
        return (a + b) / 2
    
    def newton(self, x):
        f = self.f
        oldx = x
        i = 0
        while abs(f(x)) > self.tol or abs(x - oldx) > self.tol:
            oldx = x
            if self.fp(x) == 0 or i >= 1/self.tol:
                
                return "Failed to Converge"
            x -= f(x)/self.fp(x)
            i += 1
        return x
    
    def fp(self, x, h = 0.001):
        f = self.f
        return (f(x+h) - f(x-h)) / (2*h)
    
    def trap(self, a, b, N):
        f = self.f
        w = (b-a)/N
        X = [a+w*i for i in range(N+1)]
        y = [f(x) for x in X]
        y[0] /= 2
        y[-1] /= 2
        return sum(y)*w
    
    
if __name__ == "__main__":
    c = Calc(lambda x: x**2)
    print(c.bisection(-1, 2))
    print(c.newton(5))
    print(c.trap(0,1,100), '\n')
    
    c.f = lambda x: x**2 - 1
    print(c.bisection(0, 2))
    print(c.newton(5))
    
        
        
        