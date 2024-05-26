import numpy as np
import math

class Integrator:
    def __init__(self, xMin, xMax, N):
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
    
            
    def integrate(self):       
        delx = (self.xMax - self.xMin)/self.N
        def f(x):
            return (x**2)*np.exp(-x)*np.sin(x)
        return sum((f(self.xMin + i*delx))*delx for i in range(0,self.N))

examp = Integrator(1,3,200000)
print(examp.integrate())
