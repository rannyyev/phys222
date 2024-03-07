import matplotlib.pyplot as plt
import numpy as np

wavelengths = [404.6, 435.8, 546.1, 579.1]
refractive_indices = [1.536, 1.524, 1.514, 1.511]

for i in range(len(wavelengths)):
    wavelengths[i] = 1 / wavelengths[i]**2

plt.plot(wavelengths, refractive_indices, 'o', label='Data')

m, b = np.polyfit(wavelengths, refractive_indices, 1)
x_fit = np.linspace(2*10**-6, 8*10**-6, 100)
y_fit = m * x_fit + b
plt.plot(x_fit, y_fit, label='y = {:.2e}x + {:.2f}'.format(m, b))

plt.xlabel(r'$1 / \lambda^2 \, \text{nm}^{-2}$')
plt.ylabel('Refractive index')
plt.grid()
plt.legend()
plt.title(r'Refractive index ($n$) versus $1 / \lambda^2$')

plt.savefig('f3.png', dpi=300)