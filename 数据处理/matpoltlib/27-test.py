import numpy as np

ary = np.arange(1, 37).reshape(6, 6)


def apply(data):
    data = data / 2
    return np.mean(data)


# 轴向汇总 np.apply_along_axis(fun_c,axis,ary)
r = np.apply_along_axis(apply, 1, ary)
print(r)
