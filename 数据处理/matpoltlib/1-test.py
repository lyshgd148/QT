import numpy as np
import matplotlib.pyplot as mp

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([12, 34, 4, 56, 6, 45])
mp.plot(x, y)
mp.hlines((10, 3, 2), (0, 4, 3), (6, 3, 1))
mp.vlines(3, 0, 50)

mp.show()
# 哈哈哈ha
