import matplotlib.pyplot as plt
import numpy as np

def processinputdata(filename):
    """
    Opens a text file and prints each line (row) individually.
    """
    lines = []
    with open(filename, 'r', encoding='utf-16') as file:
        for line in file:
            lines.append(line.strip().split())
    return lines

data = processinputdata('data.txt')[2:135]

x = [float(i[2]) for i in data]
y = [float(i[1]) for i in data]

plt.plot(x, y)
plt.xlabel('Angular Position (degrees)')
plt.ylabel('Intensity (a.u.)')
plt.grid()
plt.title(r'Measured intensities versus angular position ($\theta$)')
plt.savefig('plot1.png', dpi=300)