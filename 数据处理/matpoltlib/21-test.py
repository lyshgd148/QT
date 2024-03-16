import numpy as np


# 简单体验一下对数据的读取
# data = np.loadtxt('./1.csv', delimiter=',',
#                   usecols=[0, 1, 2, 3, 4],
#                   dtype=[('a', 'f8', 1), ('b', 'f8', 1), ('c', 'f8', 1), ('d', 'f8', 1), ('e', 'f8', 1)],
#                   skiprows=1)
# print(data['a'])

a, b, c, d, e = np.loadtxt('./1.csv',
                           skiprows=2,
                           delimiter=',',
                           usecols=[0, 1, 2, 3, 4],
                           dtype='f8,f8,f8,f8,f8',
                           unpack=True)
print(a)
