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

# Example usage
data = processinputdata('r2\plots\data.txt')[2:135]

x = [float(i[2]) for i in data]
y = [float(i[1]) for i in data]

plt.plot(x, y)
plt.xlabel('Angular Position (degrees)')
plt.ylabel('Intensity (a.u.)')
plt.grid()
plt.title(r'Measured Intensities versus Angular Position ($\theta)')
plt.savefig('r2\\figures\plot1.png')