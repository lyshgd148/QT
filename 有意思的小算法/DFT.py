import matplotlib.pyplot as plt
import numpy as np


def DFT(x, t, omega):
    n = len(x)
    X = []
    omega = np.arange(omega[0], omega[1], omega[2])
    for i in range(len(omega)):
        s = 0
        for j in range(n):
            s += x[j] * np.exp(-1j * omega[i] * t[j])
        X.append(2*abs(s)/n)  # 求复数的模
    return (omega, X)


x = np.arange(0, 10, 0.01)
y = np.sin(5 * x) + 4*np.cos(15 * x) + 10 * np.sin(20 * x) + np.cos(10 * x)
omega, X = DFT(x=y, t=x, omega=[-25, 25, 0.1])
plt.plot(omega, X, color='green')
plt.xticks(np.arange(-25, 25, 5))
plt.show()


# def DFT(x):
#     n = len(x)
#     X = []
#     for i in range(n):
#         s = 0
#         for j in range(n):
#             s += x[j] * np.exp(-1j *2*np.pi/n*i*j)
#         X.append(2*abs(s)/n)  # 求复数的模
#     return  X
#
#
# x = np.arange(0, 10, 0.01)
# y = np.sin(5 * x) + np.cos(15 * x) + 10 * np.sin(20 * x) + np.cos(10 * x)
# X = DFT(y)
# omega=list()
# for k in range(len(x)):
#     omega.append(2*np.pi/x[-1]*k)
# plt.plot(omega, X, color='green')
# # plt.xticks(np.arange(-25, 25, 5))
# plt.show()
