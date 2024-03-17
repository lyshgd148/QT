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
date = date[9000:]
Close = Close[9000:]
x = np.linspace(-1, 1, 5)
kernel = np.exp(x)
kernel = kernel[::-1] / np.sum(kernel)
ma5 = np.convolve(Close, kernel, 'valid')
stds = np.zeros(ma5.size)
for i in range(stds.size):
    stds[i] = np.std(Close[i:i + 5])
upper = ma5 + 2 * stds
lower = ma5 - 2 * stds
plt.xlim(date[0], date[20])
plt.plot(date[4:], ma5, label='MA-5')
plt.plot(date[4:], upper, label='upper', color='red')
plt.plot(date[4:], lower, label='lower', color='red')
plt.plot(date, Close, label='APPL')
plt.fill_between(date[4:], upper, lower, lower < upper, color='orangered', alpha=0.3)
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
#布林带
