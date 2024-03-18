import matplotlib.pyplot as plt
import numpy as np

# 用卷积来计算5日均线
date, Open, high, low, Close = np.loadtxt('./AAPL.csv',
                                          skiprows=1,
                                          unpack=True,
                                          delimiter=',',
                                          usecols=[0, 1, 2, 3, 4],
                                          dtype='M8[D],f8,f8,f8,f8'
                                          )
n = date.size
Close = Close[n - 1 - 6:]
A = np.zeros((3, 3))
for i in range(3):
    A[i,] = Close[i:i + 3]

print(A)
B=Close[3:6]

x=np.linalg.lstsq(A,B)[0]
print(np.dot(x,B))
print(Close)