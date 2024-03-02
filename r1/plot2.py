import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = [1/(404.6**2), 1/(435.8**2), 1/(546.1**2), 1/(579.1**2)]
y = [1.77, 1.78, 1.79, 1.78]

def f(x, A, B): # this is your 'straight line' y=f(x)
  return A*x + B

popt, pcov = curve_fit(f, x, y) # your data x, y to fit
print(popt) # your A and B

plt.plot(x, y, 'ro')
plt.plot(x, f(np.array(x), *popt), 'b')
plt.grid(True)
plt.show()