import numpy as np

# 二项分布
n = 200000
sample = np.random.binomial(10, 0.5, n)
# print(sample,(sample[sample == 5]).sum())
for i in range(11):
    probablity = np.count_nonzero(sample == i) / n
    print(f'p({i})=', probablity)

# 超几何分布 （一堆产品里面 抽3次不放回 抽到好的个数）
print('-' * 60)
sample = np.random.hypergeometric(7, 3, 3, n)
for i in range(4):
    probablity = np.count_nonzero(sample == i) / sample.size
    print(f'p({i})=', probablity)

#
print('-' * 60)
