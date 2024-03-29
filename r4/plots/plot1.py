import numpy as np
from matplotlib import pyplot as plt

concentration = [1, 0.5, 0.25, 0.125]
angles = [9.83, 9, 2, 1.16]
conerr = [0.01, 0.01, 0.01, 0.01]
anglerr = [2, 2, 2, 2]

m, b = np.polyfit(concentration, angles, 1)
x_fit = np.linspace(0, 1, 100)
y_fit = m * x_fit + b

m_max, b_max = np.polyfit(
    [min(concentration) + min(conerr), max(concentration) + max(conerr)],
    [min(angles) - min(anglerr), max(angles) + max(anglerr)],
    1,
)
x_max = np.linspace(
    min(concentration) + min(conerr), max(concentration) + max(conerr), 100
)
y_max = m_max * x_max + b_max

m_min, b_min = np.polyfit(
    [min(concentration) - min(conerr), max(concentration) - max(conerr)],
    [min(angles) + min(anglerr), max(angles) - max(anglerr)],
    1,
)
x_min = np.linspace(
    min(concentration) - min(conerr), max(concentration) - max(conerr), 100
)
y_min = m_min * x_min + b_min

plt.plot(x_min, y_min, "--", label="Min")
plt.plot(x_max, y_max, "--", label="Max")
plt.plot(concentration, angles, "o", label="Data")
plt.plot(x_fit, y_fit, label="Best fit")
plt.xlabel("Concentration (g\mL)")
plt.ylabel("Angle (degrees)")
plt.errorbar(
    concentration, angles, xerr=conerr, yerr=anglerr, fmt="o", capsize=5, capthick=2
)
plt.grid()
plt.legend()
plt.title("Plot of angle versus concentration")

plt.savefig("f1.png", dpi=300)
# plt.show()
