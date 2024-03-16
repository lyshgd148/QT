import matplotlib.pyplot as plt
import numpy as np

# 用卷积来计算10日均线
date, Open, high, low, Close = np.loadtxt('./AAPL.csv',
                                          skiprows=1,
                                          unpack=True,
                                          delimiter=',',
                                          usecols=[0, 1, 2, 3, 4],
                                          dtype='M8[D],f8,f8,f8,f8'
                                          )
x = np.linspace(-1, 1, 10)
kernel = np.exp(x)
kernel = kernel[::-1] / np.sum(kernel)
ma10 = np.convolve(Close, kernel, 'valid')
plt.plot(date[9:], ma10, label='MA-10')
plt.plot(date, Close, label='APPL')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
