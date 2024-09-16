import numpy as np
import matplotlib.pyplot as plt

#   y'=(x-y)y

x = np.linspace(-10, 10, 61)
y = np.linspace(-10, 10, 61)
k = []
for j in y:
    temp = []
    for i in x:
        temp.append((i - j) * j)
    k.append(temp)

X, Y = np.meshgrid(x, y)

U = []
V = []
for row in k:
    result = np.arctan(row)
    U.append((0.2 * np.cos(result)).tolist())
    V.append((0.2 * np.sin(result)).tolist())
print(V)
plt.quiver(X, Y, U, V, scale=1, scale_units='xy')
plt.axis('equal')
plt.show()

# # 创建一个网格
# x = np.linspace(-2, 2, 10)
# y = np.linspace(-2, 2, 10)
# X, Y = np.meshgrid(x, y)
# print(X)
# # 创建x和y方向上的向量场
# U = Y
# V = -X
#
# # 绘制向量场，使所有向量长度相同
# plt.quiver(X, Y, U, V, scale=1, scale_units='xy')
# plt.show()
