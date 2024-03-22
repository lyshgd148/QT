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
Close = Close[n - 100:]
date = date[n - 100:]
N = 10
pred_prices = np.zeros(100 - 2 * N)
for i in range(pred_prices.size):
    A = np.zeros((N, N))
    for j in range(N):
        A[j,] = Close[i + j:i + j + N]

    B = Close[i + N:i + 2 * N]
    x = np.linalg.lstsq(A, B)[0]
    pred_prices[i] = np.dot(x, B)
print(pred_prices.size, date.size, Close.size)
plt.plot(date, Close)
plt.plot(date[2 * N:], pred_prices, label='predict', color='orangered')
plt.legend()
plt.show()
