import numpy as np

n = 32
# 矩阵
F = np.mat('1 1 ;1 0')
for i in range(1, n):
    print((F ** i)[0, 0])
