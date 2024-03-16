import matplotlib.pyplot as mp
import numpy as np
# 刻度网格
mp.figure('刻度网格')
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(200))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
ax.grid(which='major', axis='both', linewidth=0.6, color='orangered', alpha=0.5)
ax.grid(which='minor', axis='both', linewidth=0.6, color='lightgray', alpha=0.5)
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.plot(y, 'o-')

# 半对数坐标
mp.figure('半对数坐标')
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(200))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
ax.grid(which='major', axis='both', linewidth=0.6, color='orangered', alpha=0.5)
ax.grid(which='minor', axis='both', linewidth=0.6, color='lightgray', alpha=0.5)
x = [1, 3, 5, 7, 9, 11, 13]
mp.semilogy(x, y, 'o-')

mp.show()
