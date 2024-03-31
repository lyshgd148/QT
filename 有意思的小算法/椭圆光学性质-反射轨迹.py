import matplotlib.pyplot as plt
import numpy as np

# 生成椭圆数据
x = np.linspace(-5, 5, 5000)  # x 坐标范围
y = np.linspace(-4, 4, 4000)  # y 坐标范围
X, Y = np.meshgrid(x, y)  # 创建网格坐标矩阵
Z = X ** 2 / 25 + Y ** 2 / 16  # 椭圆的方程

x = [-3]
y = [0]

k = 0.6
n = 25
x1 = (-150 * k ** 2 + np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
y1 = k * (x1 + 3)
x.append(x1)
y.append(y1)
print(x1, y1)
# x2 = (-150 * k ** 2 - np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
# y2 = k * (x2 + 3)

for i in range(n):
    if i % 2 == 0:
        k = y[i + 1] / (x[1 + i] - 3)
        x1 = (150 * k ** 2 + np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
        x2 = (150 * k ** 2 - np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
        if np.abs(x1 - x[i + 1]) > np.abs(x2 - x[i + 1]):
            y_ = k * (x1 - 3)
            x.append(x1)
        else:
            y_ = k * (x2 - 3)
            x.append(x2)
        y.append(y_)

    else:
        k = y[i + 1] / (x[i + 1] + 3)
        x1 = (-150 * k ** 2 + np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
        x2 = (-150 * k ** 2 - np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
        if np.abs(x1 - x[i + 1]) > np.abs(x2 - x[i + 1]):
            y_ = k * (x1 + 3)
            x.append(x1)
        else:
            y_ = k * (x2 + 3)
            x.append(x2)
        y.append(y_)

print(x)
print(y)
plt.contour(X, Y, Z, [1])
plt.scatter([-3, 3], [0, 0], color='orangered', zorder=3)
plt.plot(x, y)
plt.axis('equal')
plt.xlim(-7, 7)
plt.ylim(-5, 5)

plt.show()
