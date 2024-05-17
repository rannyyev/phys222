import math

import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True

theta_i = [20, 30, 40, 50, 60, 70, 80]
theta_t = [7, 10, 14, 18, 23, 30, 37]
theta_i_exp = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
I_perpendicular_exp = [43, 30, 53, 39, 55, 32, 85, 81, 97, 72, 64, 35, 45]
I_parallel_exp = [33, 22, 25, 19, 17, 9, 6, 3, 6, 7, 16, 14, 20]

r_parallel = [
    math.tan(math.radians(theta_i[i] - theta_t[i]))
    / math.tan(math.radians(theta_i[i] + theta_t[i]))
    for i in range(len(theta_i))
]
r_perpendicular = [
    math.sin(math.radians(theta_i[i] - theta_t[i]))
    / math.sin(math.radians(theta_i[i] + theta_t[i]))
    for i in range(len(theta_i))
]

y_theoretical = [(r_parallel[i] / r_perpendicular[i]) ** 2 for i in range(len(theta_i))]
y_exp = [(I_parallel_exp[i] / I_perpendicular_exp[i]) for i in range(len(theta_i_exp))]
plt.plot(
    theta_i,
    y_theoretical,
    "ro",
    label=r"$\left(r_{\parallel}/r_{\perp}\right)^2$ (theoretical data)",
)
plt.plot(theta_i, y_theoretical, "r")
plt.plot(
    theta_i_exp, y_exp, "bo", label=r"$I_{\parallel}/I_{\perp}$ (experimental data)"
)
plt.plot(theta_i_exp, y_exp, "b")
plt.xlabel(r"$\theta_i$ (degrees)")
# plt.ylabel()
plt.title(
    r"Plot of $\left(r_{\parallel}/r_{\perp}\right)^2$ and $I_{\parallel}/I_{\perp}$ vs $\theta_i$"
)
plt.legend(loc="upper right")
plt.grid(True)
# plt.show()
plt.savefig("p2.png")
