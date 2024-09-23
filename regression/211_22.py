import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# generate x and y
xdata = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
ydata1 = np.array([3.4225,5.29,7.6729,9.7344,11.6964,13.6161,15.7609,18.0625,20.1601,22.5625,24.3049,26.2144,27.9841,30.1401,32.1489,34.1056])
ydata = ydata1*(10**-6)
def func(x, a):
    y = a*x*4*0.9119*(10**-9) - a*(10**-9)*4*0.9119*20 + 42.25*(10**-6)
    return y

alpha = optimize.curve_fit(func, xdata = xdata, ydata = ydata)[0]
print(alpha)