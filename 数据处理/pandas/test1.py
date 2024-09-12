import pandas as pd
import numpy as np

# 通过ndarray创建Series对象
s = pd.Series(np.array([70.0, 50, 30, 50]))
print(s, '\n')

s1 = pd.Series(np.array([70, 50, 60, 80]), index=['张yi', '张三', '王五', '赵6'])
print(s1, s1[0], '\n')

data = {'a': 0, 'b': 1, 'c': 2}
s2 = pd.Series(data)
print(s2, s2[['a', 'c']], '\n')

s3 = pd.Series(25, index=[x for x in range(1, 13, 2)])
print(s3)

print('-' * 40)
s4 = pd.Series([10, 34, 56, 77, 44], index=[0, 1, 2, 4, 3])
print(s4[3])
