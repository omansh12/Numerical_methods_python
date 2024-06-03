import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
xdata = np.array([0, 1, 2, 3])
ydata = np.array([1.07, 3.9, 14.8, 26.8])

def SSRes(parameters):
  # In the next line of code we want to build our 
  # quadratic approximation y = ax^2 + bx + c
  # We are sending in a list of parameters so 
  # a = parameters[0], b = parameters[1], and c = parameters[2]
  yapprox = parameters[0]*xdata**2 + \
            parameters[1]*xdata + \
            parameters[2]
  residuals = np.abs(ydata-yapprox)
  return np.sum(residuals**2)


BestParameters = minimize(SSRes,[200,2,0.75])
print("The best values of a, b, and c are: \n",BestParameters.x)
# If you want to print the diagnositc then use the line below:
# print("The minimization diagnostics are: \n",BestParameters)