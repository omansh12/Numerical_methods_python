import numpy as np
from math import *
import matplotlib.pyplot as plt



# Let us loop over number of points in the interval [5,100], 3 points corresponds to Nyquist wavelength

n1 =5
n2 =100
err = np.zeros(n2-n1-1)   # vector for error
dxa = np.zeros(n2-n1-1)   # vector for dx
npl = np.zeros(n2-n1-1)   # vector for number of points per lambda


ii = -1 

for n in range (n1,n2-1):
    ii   = ii + 1
    x    = np.linspace(0,2*np.pi,n)
    dx   = x[1]-x[0]
    f    = np.sin(x)
    df   = np.cos(x)     # Analytical derivative
    
    dfn = np.zeros(n)
    # Numerical derivative of the sin function
    for i in range (1, n-1):
        dfn[i]=(f[i+1]-f[i-1])/(2*dx)
    
    # Calculate error in the interval in which numerical derivative was calculated
    err[ii] = np.sum((df[1:n-1]-dfn[1:n-1])**2)/np.sum((df[1:n-1]**2)) * 100 
    # here they have not specifically exluded the boundaries as they have already sliced the arrays
    
    dxa[ii] = dx         # dx
    npl[ii] = 2*np.pi/dx # number of points per wavelength
    

# ----------------------------------------------------------------
# Plotting error as function of dx
plt.figure(figsize=(10,6))
plt.plot(dxa,err, ls='-', color="blue")
plt.title('Error as a function of $dx$ ')
plt.xlabel('dx')
plt.ylabel('Misfit energy (%) ')
plt.grid()
plt.show()

# ----------------------------------------------------------------
# Plotting error as function of points per wavelength
plt.figure(figsize=(10,6))
plt.plot(npl,err, ls='-', color="blue")
plt.title('Error as a function of $n/\lambda$ ')
plt.xlabel('n/$\lambda$')
plt.ylabel('Misfit energy (%) ')
plt.grid()
plt.show()