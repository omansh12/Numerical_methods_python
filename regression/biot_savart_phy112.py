import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
xdata = np.arange(11)
ydata = np.array([61.3,50.5,29.3,15.5,8.2,5,2.8,1.6,1,0.7,0.5])

def SSRes(parameters):
  # In the next line of code we want to build our 
  # quadratic approximation y = ax^2 + bx + c
  # We are sending in a list of parameters so 
  # a = parameters[0], b = parameters[1], and c = parameters[2]
  yapprox = parameters[0]*( (4*3.14*(10**-7)) *20* ((2.5)**2)*(10**6)*10) / (2*(((2.5)**2+(xdata**2))**(3/2)))
  residuals = np.abs(ydata-yapprox)
  return np.sum(residuals**2)


BestParameters = minimize(SSRes,[200])
print("The best values of a, b, and c are: \n",BestParameters.x)
# If you want to print the diagnositc then use the line below:
# print("The minimization diagnostics are: \n",BestParameters)

plt.plot(xdata,ydata,'bo',markersize=5)
x = np.linspace(0,10,100)
y = BestParameters.x[0]* ( (4*3.14*(10**-7)) *20* ((2.5)**2)*(10**6)*10) / (2*(((2.5)**2+(x**2))**(3/2)))
plt.plot(x,y,'r--')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Biot savart best fit')
plt.show()