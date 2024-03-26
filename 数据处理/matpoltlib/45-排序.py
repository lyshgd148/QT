import numpy as np

ary = np.arange(1, 21)

# 普通排序
print(np.sort(ary)[::-1])

# 联合间接排序
names = np.array(['Apple', 'Huawei', 'Mi', 'Oppo', 'Vivo'])
prices = np.array([8888, 5888, 2999, 3999, 3999])
volumes = np.array([60, 110, 40, 50, 70])
indices = np.lexsort((-volumes, prices))  # volumes:次排序 （加负号 变为倒序）; prices:主排序   （升序i排列）
print(indices, names[indices])

# 插入排序   np.searchsorted(有序序列，待插序列) (返回插入位置的序号) 和 np.insert(被插序列，位置序列，待插序列)  两个一般一起用。
a = np.array([1, 2, 4, 5, 6, 8, 9])
b = np.array([7, 3])
index = np.searchsorted(a, b)
ary = np.insert(a, index, b)
print(ary)
