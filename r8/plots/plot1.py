from matplotlib import pyplot as plt
import numpy as np

f = 18
intensitiesclockwise = [1, 0.45 , 0.04 ,0 ,0 , 0.06, 0.1, 0, 0.02, 0,0,0,0,0,0,0,0,0]
intensitiescounterclockwise = [1,0.8,0.2,0,0,0.4,0.1,0.12,0.06, 0,0,0,0,0,0,0,0,0]
angles = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]

intensities = intensitiesclockwise[::-1] + intensitiescounterclockwise[1:]
angles = [-x for x in angles[::-1]] + angles[1:]

#average clockwise and counterclockwise
intensitiesaverage = [(intensitiesclockwise[i] + intensitiescounterclockwise[i])/2 for i in range(len(intensitiesclockwise))]
intensitiesaverage = intensitiesaverage[::-1] + intensitiesaverage[1:]

#plot sinx/x function
sincx = []
for i in range(len(angles)):
    if angles[i] == 0:
        sincx.append(1)
    else:
        sincx.append(np.sin(f*np.radians(angles[i]))/(f*np.radians(angles[i])))

print(len(intensities), len(angles))
plt.plot(angles, intensitiesaverage, label='average')
grid = plt.grid(True)
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity')
plt.savefig('r8/plots/plot1.png')