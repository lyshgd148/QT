#微分方程组
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义洛伦兹吸引子的微分方程
def lorenz(w, t, p, r, b):
    x, y, z = w
    return [p*(y - x), x*(r - z) - y, x*y - b*z]

# 定义时间范围
t = np.arange(0, 30, 0.01)

# 求解微分方程组
track = odeint(lorenz, [0, 1, 0], t, args=(10, 28, 3))

# 绘制 3D 轨迹
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(track[:, 0], track[:, 1], track[:, 2])
plt.show()