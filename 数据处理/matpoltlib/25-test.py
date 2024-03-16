import numpy as np

date, Open, high, low, Close, volume = np.loadtxt('./AAPL.csv',
                                                  skiprows=1,
                                                  unpack=True,
                                                  delimiter=',',
                                                  usecols=[0, 1, 2, 3, 4, 6],
                                                  dtype='M8[D],f8,f8,f8,f8,f8'
                                                  )
print(date)

min_1 = np.min(low)
max_1 = np.max(high)

min_idx = np.argmin(low)  # 找最小值的索引
max_idx = np.argmax(high)  # 找最大值的索引

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10)[::-1].reshape(3, 3)
max_2 = np.maximum(a, b)  # 两个数组中最大的合在一起
min_2 = np.minimum(a, b)  # 两个数组中最小的合在一起

print(min_1, max_1, min_idx, max_idx, max_2, min_2, sep='~')

## 中位数的两种做法:
# way1
median1 = np.median(Close)

# way2
sorted_Close = np.sort(Close)
size = sorted_Close.size
median2 = (sorted_Close[(size - 1) // 2] + sorted_Close[size // 2]) / 2

print(median1, median2)

## 计算总体标准差 两种方法
# way1
std1 = np.std(Close)

# way2
mean1 = np.mean(Close)
d1 = (Close - mean1)
v1 = np.mean(d1 ** 2)
print(std1, '  ', np.sqrt(v1))

# #计算样本标准差
# way1
std2 = np.std(Close, ddof=1)

# way2
mean2 = np.mean(Close)
d2 = (Close - mean1)
v2 = np.sum(d2 ** 2) / (d2.size - 1)
print(std2, '  ', np.sqrt(v2))
