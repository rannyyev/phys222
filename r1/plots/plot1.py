from matplotlib import pyplot as plt
import numpy as np

wavelengths = [404.6, 435.8, 546.1, 579.1]
refractive_indices = [1.536, 1.524, 1.514, 1.511]

m, b = np.polyfit(wavelengths, refractive_indices, 1)
x_fit = np.linspace(400, 600, 100)
y_fit = m * x_fit + b

plt.plot(wavelengths, refractive_indices, 'o', label='Data')
plt.plot(x_fit, y_fit, label='Best fit line')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Refractive index')
plt.grid()
plt.legend()
plt.title(r'Refractive index ($n$) versus wavelength ($\lambda$)')

plt.savefig('f2.png', dpi=300)