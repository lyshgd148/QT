import math as m
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def grad(x, y):  # 随机生成梯度函数
    vec = list()
    vec.append(m.sin(x * 127.1 + y * 311.7) * 43758.5453123)
    vec.append(m.sin(x * 269.5 + y * 183.3) * 43758.5453123)

    for i in range(2):
        vec[i] = (vec[i] - m.floor(vec[i])) * 2 - 1
    mod = m.sqrt(vec[0] ** 2 + vec[1] ** 2)
    vec[0] = vec[0] / mod
    vec[1] = vec[1] / mod
    return vec


def perlin(x, y):
    #   p1-------p2
    #   |         |
    #   |         |
    #   |         |
    #   p0-------p3

    p0x = m.floor(x)  #
    p0y = m.floor(y)
    p1x = p0x  #
    p1y = p0y + 1
    p2x = p0x + 1  #
    p2y = p0y + 1
    p3x = p0x + 1  #
    p3y = p0y

    g0x = grad(p0x, p0y)[0]  #
    g0y = grad(p0x, p0y)[1]
    g1x = grad(p1x, p1y)[0]  #
    g1y = grad(p1x, p1y)[1]
    g2x = grad(p2x, p2y)[0]  #
    g2y = grad(p2x, p2y)[1]
    g3x = grad(p3x, p3y)[0]  #
    g3y = grad(p3x, p3y)[1]

    v0x = x - p0x  # P0点的方向向量
    v0y = y - p0y
    v1x = x - p1x  # P1点的方向向量
    v1y = y - p1y
    v2x = x - p2x  # P2点的方向向量
    v2y = y - p2y
    v3x = x - p3x  # P3点的方向向量
    v3y = y - p3y

    product0 = g0x * v0x + g0y * v0y  # P0点梯度向量和方向向量的点乘
    product1 = g1x * v1x + g1y * v1y
    product2 = g2x * v2x + g2y * v2y
    product3 = g3x * v3x + g3y * v3y

    # p1,p2插值
    t = 6 * (x - p0x) ** 5 - 15 * (x - p0x) ** 4 + 10 * (x - p0x) ** 3
    n0 = product1 * (1 - t) + product2 * t
    # p0,p3插值
    n1 = product0 * (1 - t) + product3 * t
    # p点插值
    t = 6 * (y - p0y) ** 5 - 15 * (y - p0y) ** 4 + 10 * (y - p0y) ** 3
    n1 = n1 * (1 - t) + n0 * t
    return n1


def mapping(lst):
    return [255 * (x + 1) / 2 for x in lst]


size = 1024

x = np.linspace(0, 8, size)
y = np.linspace(0, 8, size)
X, Y = np.meshgrid(x, y)
Z = list()
ls = list()
for i in range(size):
    ls = []
    for j in range(size):
        ls.append(perlin(x[j], y[i]))
    Z.append(ls)
Z = list(map(mapping, Z))
Z = np.array(Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', rstride=10, cstride=10)
# surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.show()
