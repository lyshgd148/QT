# 在进行 第三类积分运算时 我无意间发现了一个好玩的东西--因此想写一个程序来大概的验证一下！
import numpy as np


def prod(n):
    arr = np.arange(1, n + 1)
    temp = 0
    for i in range(n):
        if i % 2 == 0:
            temp = temp + 1 / np.prod(arr[:i + 1])
        else:
            temp = temp - 1 / np.prod(arr[:i + 1])
    print('1-1/e', ':', (1 - 1 / np.e))
    print('temp', ':', temp)


prod(33)
