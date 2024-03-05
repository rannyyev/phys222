from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

x = [404.6, 435.8, 546.1, 579.1]
y = [1.77, 1.78, 1.79, 1.78]

f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(400, 600, 1000)
y_new = f(x_new)

plt.figure(figsize = (10,8))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Refractive Index of Prism vs Wavelength')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Refractive Index')
plt.grid(True)
plt.show()