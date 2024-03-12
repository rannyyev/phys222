import matplotlib.pyplot as plt
import numpy as np

with open('data.txt') as f:
    data = f.read()

data = data.split('\n')
x = [row.split(' ')[0] for row in data]
print(x)