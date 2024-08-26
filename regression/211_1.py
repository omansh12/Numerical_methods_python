import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
xdata = np.array([0, 1/20, 1/15, 1/10 , 1/5])
ydata = np.array([0, 6.19, 7.7, 11.42, 23.92])

def SSRes(parameters):
  # In the next line of code we want to build our 
  # quadratic approximation y = ax^2 + bx + c
  # We are sending in a list of parameters so 
  # a = parameters[0], b = parameters[1], and c = parameters[2]
  yapprox = parameters[0]*xdata
  residuals = np.abs(ydata-yapprox)
  return np.sum(residuals**2)


BestParameters = minimize(SSRes,[200])
print("The best values of a, b, and c are: \n",BestParameters.x)
# If you want to print the diagnositc then use the line below:
# print("The minimization diagnostics are: \n",BestParameters)

plt.plot(xdata,ydata,'bo',markersize=5)
x = np.linspace(0,0.2,100)
y = BestParameters.x[0]*x
plt.plot(x,y,'r--')
plt.grid()
plt.xlabel('concentration (gm/cc)')
plt.ylabel('theta (degrees)')
plt.title('θ vs c best fit (slope = 118.51609797)')
plt.show()