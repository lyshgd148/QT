# 用三角函数 合成方波

import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.zeros(1000)
for i in range(1, n + 1):
    y += 4 * np.pi / (2 * n - 1) * np.sin((2 * n - 1) * x)

plt.figure()
plt.plot(x, y)
plt.show()
