import numpy as np

ary = np.arange(0, 10)
print(ary, ary.dtype, ary.shape)

ary = ary.astype(float)
print(ary)

ary = np.array([[1, 2, 3], [4, 5, 6]])
print(ary, ary.dtype, ary.shape)
ary = ary.astype(float)
ary.shape = (3, 2)
print(ary, ary.shape, ary.dtype, '"size":', ary.size, '"len":', len(ary))

print('*' * 50)
ary = np.arange(1, 28)
ary.shape = (3, 3, 3)
print(ary)
print('*' * 50)
print(ary[0])
print('*' * 50)
print(ary[0][2])
print('*' * 50)
print(ary[0][2][2])
print(ary[0, 2, 2])
print(ary.shape)
print(ary.shape[0])
print("*" * 60)
# 遍历三维数组
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i, j, k])
