import math
import matplotlib.pyplot as plt

theta_i = [20,30,40,50,60,70,80]
theta_t = [7,10,14,18,23,30,37]
theta_i_exp = [20,25,30,35,40,45,50,55,60,65,70,75,80]
I_perpendicular_exp = [43,30,53,39,55,32,85,81,97,72,64,35,45]
I_parallel_exp = [33,22,25,19,17,9,6,3,6,7,16,14,20]

#(I_paralel / I_perpendicular)^2  vs theta_i

I_parallel_theoretical = [math.tan(math.radians(theta_i[i]-theta_t[i]))/math.tan(math.radians(theta_i[i]+theta_t[i])) for i in range(len(theta_i))]
I_perpendicular_theoretical = [math.sin(math.radians(theta_i[i]-theta_t[i]))/math.sin(math.radians(theta_i[i]+theta_t[i])) for i in range(len(theta_i))]

y_theoretical = [(I_parallel_theoretical[i]/I_perpendicular_theoretical[i])**2 for i in range(len(theta_i))]
y_exp = [(I_parallel_exp[i]/I_perpendicular_exp[i])**2 for i in range(len(theta_i_exp))]
plt.plot(theta_i, y_theoretical, 'ro', label='Theoretical Data')
plt.plot(theta_i, y_theoretical, 'r')
plt.plot(theta_i_exp, y_exp, 'bo', label='Experimental Data')
plt.plot(theta_i_exp, y_exp, 'b')
plt.xlabel('$\\theta_i$ - Incident Angle (degrees)')
plt.ylabel('$(I_{parallel}/I_{perpendicular})^2$')
plt.legend()
plt.grid()
plt.savefig('p2.png')