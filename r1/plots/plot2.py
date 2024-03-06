import matplotlib.pyplot as plt
import numpy as np

wavelengths = [404.6, 435.8, 546.1, 579.1]
refractive_indices = [1.5357, 1.5243, 1.5144, 1.5111]

for i in range(len(wavelengths)):
    wavelengths[i] = 1 / wavelengths[i]**2

plt.plot(wavelengths, refractive_indices, 'o', label='Data')

m, b = np.polyfit(wavelengths, refractive_indices, 1)
x_fit = np.linspace(2*10**-6, 8*10**-6, 100)
y_fit = m * x_fit + b
plt.plot(x_fit, y_fit, label='y = {:.2e}x + {:.2f}'.format(m, b))

plt.xlabel('1/λ^2 (nm^-2)')
plt.ylabel('Refractive index')
plt.grid()
plt.legend()
plt.title('Refractive index(n) vs 1/λ^2')

plt.savefig('refractive_index_vs_1_over_lambda_squared.png')