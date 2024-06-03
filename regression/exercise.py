import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def my_lin_regression(f, x, y):
    # Create a matrix A where each column is a basis vector evaluated at each x
    A = np.vstack([func(x) for func in f]+[np.ones(len(x))]).T

    # Use numpy's least squares function to solve for the best parameters
    beta, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

    return beta

x = np.linspace(0, 2*np.pi, 1000)
y = 3*np.sin(x) - 2*np.cos(x) + np.random.random(len(x))
f = [np.sin, np.cos]
beta = my_lin_regression(f, x, y)

plt.figure(figsize = (10,8))
plt.plot(x,y,'b.', label = 'data')
plt.plot(x, beta[0]*f[0](x)+beta[1]*f[1](x)+beta[2], 'r', label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Square Regression Example')
plt.legend()
plt.show()  