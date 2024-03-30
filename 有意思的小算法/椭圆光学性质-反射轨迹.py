import matplotlib.pyplot as plt
import numpy as np

# 生成椭圆数据
x = np.linspace(-5, 5, 500)  # x 坐标范围
y = np.linspace(-4, 4, 400)  # y 坐标范围
X, Y = np.meshgrid(x, y)  # 创建网格坐标矩阵
Z = X ** 2 / 25 + Y ** 2 / 16  # 椭圆的方程

plt.contour(X, Y, Z, [1])
plt.axis('equal')
plt.xlim(-7, 7)
plt.ylim(-5, 5)

plt.show()
