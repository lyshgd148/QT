# 改版计算阶乘结果末尾几个连续的零
def Cum_NUm(n):
    num = 0
    time = 1
    while n // (5 ** time):
        num += (n // (5 ** time))
        time += 1
    return num


end = 10000
num = list()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, end, end)
for i in range(1, end + 1):
    num.append(Cum_NUm(i))

plt.plot(x, num)
plt.grid()
plt.show()
