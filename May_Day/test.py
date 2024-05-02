import numpy as np
import matplotlib.pyplot as plt
import copy


def elliptic(a, b):
    x = np.linspace(0, a, 1000)
    y = b * np.sqrt(1 - (x ** 2 / a ** 2))
    y1 = copy.deepcopy(y)
    x1 = copy.copy(x)
    y1 = y1[::-1]
    x1 = -x1
    x1 = x1[::-1]
    x = np.hstack((x1, x))
    y = np.hstack((y1, y))
    x1 = copy.copy(x)
    y1 = copy.copy(y)
    x1 = -x1
    y1 = -y1
    x = np.hstack((x, x1))
    y = np.hstack((y, y1))
    return x, y


x1 = np.zeros(300)
x1 += 10
y1 = np.linspace(40, 25, 300)

x2 = np.linspace(10, 15, 300)
y2 = np.zeros(300)
y2 += 25
x, y = elliptic(15, 20)

index_i1 = 0
index_j1 = 0

num = 1000000
for i in range(300):
    for j in range(4000):
        num1 = np.sqrt((x1[i] - x[j]) ** 2 + (y1[i] - y[j]) ** 2)
        if num > num1:
            num = num1
            index_i1, index_j1 = i, j

index_i2 = 0
index_j2 = 0
num_ = 100000
for i in range(300):
    for j in range(4000):
        num1 = np.sqrt((x2[i] - x[j]) ** 2 + (y2[i] - y[j]) ** 2)
        if num_ > num1:
            num_ = num1
            index_i2, index_j2 = i, j

print(x[index_j1], y[index_j1])
ax = plt.gca()
ax.set_aspect(1)
plt.plot(x, y, color='black')
plt.plot(x1, y1, color='black')
plt.plot(x2, y2, color='black')
plt.plot([x1[index_i1], x[index_j1]], [y1[index_i1], y[index_j1]], color='red')
plt.plot([x2[index_i2], x[index_j2]], [y2[index_i2], y[index_j2]], color='red')
plt.show()
