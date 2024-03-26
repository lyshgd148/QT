# 目前只会线性插值,三次样条插值还未了解。
import matplotlib.pyplot as plt
import numpy as np


def interpolate(start, end, num):
    s_x, s_y = start
    e_x, e_y = end
    k = (e_y - s_y) / (e_x - s_x)
    step = (e_x - s_x) / (n + 1)
    # print('k:', k, 'step:', step)
    x_ = np.linspace(s_x + step, e_x - step, num)
    y_ = k * (x_ - s_x) + s_y
    return x_.tolist(), y_.tolist()


n = 15
dis_x = np.linspace(-50, 50, n)
dis_y = np.sinc(dis_x)

x = list()
y = list()
for i in range(n - 1):
    a, b = interpolate((dis_x[i], dis_y[i]), (dis_x[i + 1], dis_y[i + 1]), 8)
    x.extend([dis_x[i]] + a)
    y.extend([dis_y[i]] + b)
x.append(dis_x[-1])
y.append(dis_y[-1])
print(x)
print(y)
x = np.array(x)
y = np.array(y)
plt.scatter(dis_x, dis_y, color='red')
plt.plot(x, y)
plt.show()

# print(np.linspace(1,2,3))
