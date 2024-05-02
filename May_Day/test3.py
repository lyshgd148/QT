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


x, y = elliptic(15, 20)

index = 0
index1 = 0
num = 1000000
x1 = [-12, -12, 9, 11]
y1 = [-13, 12, 14, -6]
for j in range(4):
    for i in range(4000):
        num1 = np.sqrt((x1[j] - x[i]) ** 2 + (y1[j] - y[i]) ** 2)
        if num1 < num:
            num = num1
            index1 = i
            index = j

print(num, index)
ax = plt.gca()
ax.set_aspect(1)
plt.plot(x, y, color='black')
plt.plot([x1[index], x[index1]], [y1[index], y[index1]], color='red', linewidth=3)
plt.show()
