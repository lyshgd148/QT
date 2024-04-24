import numpy as np
import matplotlib.pyplot as plt

# 以 1/(1+x^2) 在0处的泰勒展开 并却在区间(0,1)处进行验证！

x = np.linspace(0, 1, 100000)


def taylor(x, n):
    result = np.zeros_like(x)
    temp = np.zeros((1, n))
    temp[0, [i for i in range(n) if i % 2 == 0]] = 1
    temp[0, [i for i in range(n) if i % 2 == 1]] = -1
    for i in range(0, n):
        result += temp[0, i] * x ** (2 * i)
    return result


y = taylor(x, 100000)

plt.plot(x, 1 / (1 + x ** 2), label=r'$\frac{1}{1+x^2}$')
plt.plot(x, y, label=r'$\sum_{i=0}^{1000} (-1)^{i}x_i^{2i}$')
plt.legend()
plt.show()

# 这个结果说明 当 1/(1+x^2)在0处的泰勒展开的次数足够多的时侯 在区间(0,1)时 除了在x=1时会跳变到0或1 其余的区间处可认为完全重合
