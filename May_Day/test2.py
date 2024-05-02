import numpy as np
import matplotlib.pyplot as plt
import copy

#创建椭圆
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

#同test1
index = 0
num = 1000000
for i in range(4000):
    num1 = np.sqrt((11 - x[i]) ** 2 + (6.5 - y[i]) ** 2)
    if num > num1:
        num = num1
        index = i
print(num,x[index],y[index])
ax = plt.gca()
ax.set_aspect(1)
plt.plot(x, y, color='black')
plt.plot([11, x[index]], [6.5, y[index]], color='red')
plt.show()
