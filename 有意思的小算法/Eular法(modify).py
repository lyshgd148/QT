import matplotlib.pyplot as plt
import numpy as np

# y'+xy=x   y'=x(1-y)
x_ = 0
y_ = 2


def f(x, y, dx):
    return y + x * (1 - y) * dx


def Eular(x, y, dx, end):
    temp_y = []
    temp_x = []
    for i in range(int(end // dx)):
        temp_x.append(x)
        k = ((x + dx)*(1 - f(x, y, dx)) + x * (1 - y)) / 2
        y = y + k * dx
        x = x + dx
        temp_y.append(y)
    return temp_x, temp_y


x, y = Eular(0, 2, 0.01, 10)

plt.figure()
plt.plot(x, y)
X = np.linspace(0, 10, 1001)
Y = np.exp(-0.5 * X ** 2) + 1
plt.plot(X, Y)
plt.show()
