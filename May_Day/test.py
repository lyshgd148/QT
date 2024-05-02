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
print(x.shape)
ax = plt.gca()
ax.set_aspect(1)
plt.plot(x, y)
plt.show()
