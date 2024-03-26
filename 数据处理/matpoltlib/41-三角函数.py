# # 用三角函数 合成方波
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# n = 100000
# x = np.linspace(-2 * np.pi, 2 * np.pi, 10000)
# y = np.zeros(10000)
# for i in range(1, n + 1):
#     y += ((4 * np.pi / (2 * i - 1)) * np.sin((2 * i - 1) * x))
#
# plt.figure()
# plt.plot(x, y)
# plt.show()


# 采样定理的一些测试
import numpy as np
import matplotlib.pyplot as plt

n = 1000
# x = np.linspace(0, 1, 1001)
x = np.array([x / 1000+1/2500 for x in range(1, 1001)])
y = np.sin(n * 2 * np.pi * x)
plt.ylim(-0.01, 0.01)
plt.plot(x, y)
plt.show()
