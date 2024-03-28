from matplotlib import pyplot as plt
import numpy as np

concentration = [1, 0.5, 0.25, 0.125]
angles = [9.83,9,2,1.16]

m, b = np.polyfit(concentration, angles, 1)
x_fit = np.linspace(0, 1, 100)
y_fit = m * x_fit + b

plt.plot(concentration, angles, 'o', label='Data')
plt.plot(x_fit, y_fit, label='Best fit line')
plt.xlabel('concentration')
plt.ylabel('angle')
plt.grid()
plt.legend()
plt.title('angle vs concentrations')

plt.savefig('f2.png', dpi=300)