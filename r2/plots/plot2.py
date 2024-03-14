import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def processinputdata(filename):
    """
    Opens a text file and prints each line (row) individually.
    """
    lines = []
    with open(filename, 'r', encoding='utf-16') as file:
        for line in file:
            lines.append(line.strip().split())
    return lines

data = processinputdata('r2\plots\data.txt')[2:135]

x = [float(i[2]) for i in data]
y = [float(i[1]) for i in data]

def cos_squared_func(x, amp, omega, phi):
  # Convert degrees to radians
  x_rad = np.radians(x)
  return amp * np.cos(omega * x_rad + phi) ** 2


popt, pcov = curve_fit(cos_squared_func, x, y)
print("Fitted parameters:", popt)

x_fit = np.linspace(min(x), max(x), 100)
y_fit = cos_squared_func(x_fit, *popt)

plt.plot(x, y, 'o', label='Data')
plt.plot(x_fit, y_fit, '-', label='Fitted curve')
plt.legend()
plt.xlabel('Angular Position (degrees)')
plt.ylabel('Intensity (a.u.)')
plt.grid()
plt.title(r'Measured intensities versus angular position ($\theta$)')
plt.savefig('plot2.png', dpi=300)