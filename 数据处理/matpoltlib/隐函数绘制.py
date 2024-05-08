import numpy as np
import matplotlib.pyplot as plt


def implicit_function(x, y):
    return np.sin(x) - np.cos(x * y)  # 这个隐函数还是有意思的


x = np.linspace(-10, 10, 10000)
y = np.linspace(-10, 10, 10000)
X, Y = np.meshgrid(x, y)

Z = implicit_function(X, Y)

plt.contour(X, Y, Z, [0], colors='r')  # 绘制隐函数曲线
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
