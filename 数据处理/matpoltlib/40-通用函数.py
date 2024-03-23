import numpy as np

# n = 32
# # 矩阵
# F = np.mat('0 1 ;1 -1')
# # for i in range(1, n):
# #     print((F ** i)[0, 0])
#
# print(F ** 19)
#
# F = np.mat('1 1 ;1 0')
# print(F ** -19)


a = np.arange(1, 10)
# 数组的裁剪  ndarray.clip(min=,max=) 返回数组 原来的数组不变
print(np.clip(a, 3, 8))

# 数组的压缩  ndarray.compress(条件) 返回满足体条件的元素组成的新数组
print(np.compress(a > 5, a))
print(a[a > 5])
print(a[(a > 3) & (a <= 7)])
