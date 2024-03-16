import numpy as np

ary0 = np.arange(1, 7).reshape(2, 3)
ary1 = np.arange(7, 13).reshape(2, 3)
print(ary0, 'ary0')
print(ary1, 'ary1')

# 水平组合与拆分
ary = np.hstack((ary0, ary1))
print(ary, 'ary')
ary3, ary4 = np.hsplit(ary, 2)
print(ary3, 'ary3')
print(ary4, 'ary4')

print("-" * 60)

# 垂直组合与拆分
ary = np.vstack((ary0, ary1))
print(ary, 'ary')
ary3, ary4 = np.vsplit(ary, 2)
print(ary3, 'ary3')
print(ary4, 'ary4')

print("-" * 60)

# 深度方向组合与拆分
ary = np.dstack((ary0, ary1))
print(ary, 'ary')
ary3, ary4 = np.dsplit(ary, 2)
print(ary3, 'ary3')
print(ary4, 'ary4')
ary4.shape = (2, 3)
print(ary4)
print("-" * 60)

# 组合拆分通用方法 np.concatenate((a,b),axis=0/1/2) np.split(c,2,aixs=0/1/2) [0:垂直,1:水平,2:深度]
ary = np.concatenate((ary0, ary1), axis=0)
print(ary)
ary3, ary4 = np.split(ary, 2, axis=0)
print(ary3, 'ary3')
print(ary4, 'ary4')
print("-" * 60)

# 一维数组 其他组合方案
a = np.arange(1, 9)
b = np.arange(9, 17)
print(np.row_stack((a, b)))
print(np.column_stack((a, b)))
print("*" * 60)

# 不同 长度的数组的组合
a = np.arange(1, 9)
b = np.arange(9, 16)
print(a.shape, type(a.shape))
print(b.shape)
b = np.pad(b, pad_width=(0, 1), mode='constant', constant_values=999)
print(b, '    ', b.shape)
