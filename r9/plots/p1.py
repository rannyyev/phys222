import math

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["text.usetex"] = True

theta_i = np.linspace(20, 80, 7)
theta_t = [7, 10, 14, 18, 23, 30, 37]

sin_theta_i = [math.sin(math.radians(i)) for i in theta_i]
sin_theta_t = [math.sin(math.radians(i)) for i in theta_t]

fig, ax = plt.subplots(tight_layout=True)
plt.scatter(sin_theta_t, sin_theta_i, label="Data", marker="o")

m, b = np.polyfit(sin_theta_t, sin_theta_i, deg=1)

plt.axline(xy1=(0, b), slope=m, color="green", label="Best fit", linestyle="--")
plt.xlabel(r"$\sin(\theta_t)$")
plt.ylabel(r"$\sin(\theta_i)$")
plt.title(r"$\sin(\theta_i)$ vs $\sin(\theta_t)$")
plt.legend(loc="upper left")
plt.grid(True)

print(m, b)
# plt.savefig("p1.png", dpi=300)
