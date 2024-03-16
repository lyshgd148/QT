import numpy as np
import matplotlib.pyplot as plt

n = 200
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
# 散点图
plt.figure('3D1')
ax3d = plt.axes(projection='3d')
d = x ** 2 + y ** 2 + z ** 2
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
ax3d.scatter(x, y, z, s=30, marker='o', c=d, cmap='jet_r')
# 曲面图
plt.figure('3D2')
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * \
    np.exp(-x ** 2 - y ** 2)
ax3d1 = plt.axes(projection='3d')
# ax3d1.plot_surface(x, y, z, cstride=10, rstride=10,cmap='jet')
ax3d1.plot_surface(x, y, z)
# 线框图
plt.figure('3D3')
ax3d2 = plt.axes(projection='3d')
# ax3d2.plot_wireframe(x, y, z, cstride=10, rstride=10, linewidth=0.8, color='dodgerblue')
# ax3d2.plot_wireframe(x, y, z, linewidth=0.8, color='dodgerblue')
# ax3d2.plot_wireframe(x, y, z, color='dodgerblue')
ax3d2.plot_wireframe(x, y, z)
plt.show()
