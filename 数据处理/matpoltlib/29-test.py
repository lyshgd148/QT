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
kernel = np.ones(10) / 10
ma10 = np.convolve(Close, kernel, 'valid')
plt.plot(date[9:], ma10, label='MA-10')
plt.plot(date, Close, label='APPL')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
