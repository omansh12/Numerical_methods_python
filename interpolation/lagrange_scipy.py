import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

from scipy.interpolate import lagrange
x = [0, 1, 2]
y = [1, 3, 2]
f = lagrange(x, y)
x_new = np.arange(-1.0, 3.1, 0.1)
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()