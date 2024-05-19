import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
s = np.linspace(0, 2 * np.pi, 1000)

T, S = np.meshgrid(t, s)

result_x = 3 * np.cos(T) + np.cos(T) * np.cos(S)  # x=3cos(t)+cos(t)cos(s)
result_y = 3 * np.sin(T) + np.sin(T) * np.cos(S)  # y=3sin(t)+sin(t)cos(s)
result_z = np.sin(S)  # z=sin(s)

figure = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(result_x, result_y, result_z, rstride=8, cstride=8, cmap='rainbow')
ax.axis('equal')
ax.axis('off')
plt.show()
