import numpy as np
import matplotlib.pyplot as mp


def random_color():
    r = np.random.rand()
    g = np.random.rand()
    b = np.random.rand()
    return r, g, b


cap = tuple()
colors = list()
values = [26, 17, 21, 29, 21]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JS', 'C++', 'Java', 'PHP']
for i in range(len(values)):
    cap = random_color()
    colors.append(cap)

mp.figure('Pie', facecolor='gray')
mp.pie(values, spaces, labels, colors, "%.1f%%")
mp.axis('equal')
mp.legend()
mp.show()
