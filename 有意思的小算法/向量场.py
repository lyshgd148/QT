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

