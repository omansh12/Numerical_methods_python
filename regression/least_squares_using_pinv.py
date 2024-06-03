import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

#plt.style.use('seaborn-poster')
# generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T

# turn y into a column vector
y_ = y[:, np.newaxis], # although matrix and array multiplication is allowed but this makes y into a matrix and 
# in result we get Beta as a matrix to be consistent with the derivation and theoreitical stuff

# Direct least square regression
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y_)
print(alpha)


#use the pseudo inverse
pinv = np.linalg.pinv(A)
alpha = pinv.dot(y)
print(alpha)

# plot the results
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()