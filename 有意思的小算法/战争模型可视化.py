import matplotlib.pyplot as plt
import numpy as np

a = 4
b = 1


def implicit_function(x, y):
    return 4 * y ** 2 - b * x ** 2 - y  # 这个隐函数还是有意思的


x = np.linspace(0, 5, 10000)
y = np.linspace(0, 5, 10000)
X, Y = np.meshgrid(x, y)

Z = implicit_function(X, Y)

plt.contour(X, Y, Z, [-10, -5, -1,-0.001, 0, 1, 5, 10], colors='black', linestyles='solid')  # 绘制隐函数曲线
plt.text(1.66, 2.25, 'k>0', fontsize=12)
plt.text(0.184, 0.175, 'k=0', fontsize=12)
plt.text(3.47, 0.44, 'k<0', fontsize=12)

plt.arrow(*(2.20, 2.07), *(1.61 - 2.20, 1.92 - 2.07), head_width=0.09, fc='black')
plt.arrow(*(2.28, 1.71), *(1.61 - 2.28, 1.5 - 1.71), head_width=0.09, fc='black')
plt.arrow(*(2.35, 1.42), *(1.59 - 2.35, 1.06 - 1.42), head_width=0.09, fc='black')
#
plt.arrow(*(1.07, 0.69), *(0.52 - 1.07, 0.42 - 0.69), head_width=0.09, fc='black')
#
plt.arrow(*(2.39, 1.22), *(1.53 - 2.39, 0.71 - 1.22), head_width=0.09, fc='black')
plt.arrow(*(3.1, 1.18), *(2.42 - 3.1, 0.64 - 1.18), head_width=0.09, fc='black')
plt.arrow(*(3.96, 1.34), *(3.39 - 3.96, 0.79 - 1.34), head_width=0.09, fc='black')

plt.axis('equal')
plt.xlim(0.1, 5)
plt.ylim(0.1, 4)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
# plt.xticks([])
# plt.yticks([])
# plt.grid(True)
plt.show()
