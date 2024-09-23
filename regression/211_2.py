import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
xdata = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
ydata1 = np.array([3.4225,5.29,7.6729,9.7344,11.6964,13.6161,15.7609,18.0625,20.1601,22.5625,24.3049,26.2144,27.9841,30.1401,32.1489,34.1056])
ydata = ydata1*(10**-6)
def SSRes(parameters):
  # In the next line of code we want to build our 
  # quadratic approximation y = ax^2 + bx + c
  # We are sending in a list of parameters so 
  # a = parameters[0], b = parameters[1], and c = parameters[2]
  yapprox = parameters[0]*xdata*4*0.9119*(10**-9) - parameters[0]*(10**-9)*4*0.9119*20 + 42.25*(10**-6)
  residuals = np.abs(ydata-yapprox)
  return np.sum(residuals**2)


BestParameters = minimize(SSRes,[557.02461134])
print("The best values of a, b, and c are: \n",BestParameters.x)
# If you want to print the diagnositc then use the line below:
# print("The minimization diagnostics are: \n",BestParameters)

plt.rcParams.update({'font.size':12})
plt.plot(xdata,ydata,'ko',markersize=5)

x = np.linspace(1,16,100)
y = BestParameters.x[0]*x*4*0.9119*(10**-9) - BestParameters.x[0]*(10**-9)*4*0.9119*20 + 42.25*(10**-6)
plt.plot(x,y,'k--')
plt.grid()
plt.xlabel('Ring number (n)',fontsize = 15)
plt.ylabel('Dₙ² (10⁻⁶ m²)',fontsize = 15)
plt.title('Dₙ² vs n best fit (λ = 557.02461134)',fontsize = 15)
plt.show()