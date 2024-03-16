import numpy as np

# 数组的其他属性
ary = np.array([[1 + 1j, 2 + 2j, 3 + 3j],
                [4 + 4j, 5 + 5j, 6 + 6j],
                [7 + 7j, 8 + 8j, 9 + 9j]])

print(ary.shape)
print(ary.dtype)
print(ary.itemsize)
print(ary.size)
print(ary.nbytes)
print(ary.real)
print(ary.imag)
print(ary.T)
print([x for x in ary.flat])