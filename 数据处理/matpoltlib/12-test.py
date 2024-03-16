import numpy as np
import matplotlib.pyplot as mp

# x = np.linspace(-5, 5, 10)
# y = np.linspace(-3, 3, 6)
# X, Y = np.meshgrid(x, y) #6行10列

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * \
    np.exp(-x ** 2 - y ** 2)
mp.figure(facecolor='lightgray')
cntr = mp.contour(x, y, z, 10 * 2 - 5, colors='black', linewidths=0.5)
mp.contourf(x, y, z, 50, cmap='jet')
mp.clabel(cntr, fmt='%.2f', inline_spacing=1, fontsize=8)
mp.grid(linestyle=':')
# mp.axis('equal')
mp.show()
