import matplotlib.pyplot as mp
import numpy as np

n = 50000000
num = np.random.normal(75, 7, n)
num = np.round(num, decimals=1)
values, counts = np.unique(num, return_counts=True)
mp.figure('np.random.normal正态分布的验证', facecolor='lightgray')
print(values, counts)
mp.plot(values, counts)
mp.show()
