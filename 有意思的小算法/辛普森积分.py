import numpy as np


# 假设要进行数值计算的函数是 y=exp(-x) 对区间(1,10)进行积分

# sin(x)默认是弧度单位
def Function(x):
    return np.sin(x)/np.array(x)


def simpson(a, b, n):
    a = np.array(a)
    b = np.array(b)
    ai_fa = (b - a) / (6 * n)

    f1 = Function(a) + Function(b)
    f2 = 0
    f3 = 0
    for i in range(n - 1):
        f2 = f2 + 2 * Function(a + ((b - a) / n) * (i + 1))
    for i in range(n):
        f3 = f3 + 4 * Function(a + ((b - a) / (2 * n)) * (2 * i + 1))
    result = ai_fa * (f1 + f2 + f3)
    return result


result = simpson(1, 10, 100000)
print(result)
