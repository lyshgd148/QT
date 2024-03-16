import numpy as np

# list1 = list(range(10))
# for i in list1:
#     print(id(i))

a = np.array([1, 2, 3, 4, 5])
print(a)

a = np.arange(0, 10, 2)
print(a)

a = np.zeros(10, dtype=float)
print(a, a.dtype)

a = np.ones((3, 3), dtype='int32')
print(a, a.dtype, a.shape)
#
# a = np.ones(5, dtype='float32') * (1 / 5)
# print(a, a.dtype)

print(np.zeros_like(a))  # 维度相似
print(np.ones_like(a))
