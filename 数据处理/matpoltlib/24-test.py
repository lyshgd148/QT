import matplotlib.pyplot as plt
import numpy as np

# K线图
date, Open, high, low, Close, volume = np.loadtxt('./AAPL.csv',
                                                  skiprows=1,
                                                  unpack=True,
                                                  delimiter=',',
                                                  usecols=[0, 1, 2, 3, 4, 6],
                                                  dtype='M8[D],f8,f8,f8,f8,f8'
                                                  )
# 均值
mean = np.mean(Close)
rise = Close > Open
# 加权平均vwap
vwap = np.average(Close, weights=volume)
# twap
time = np.linspace(1, 100, date.size)
twap = np.average(Close, weights=time)
# K线
color = np.zeros(rise.size, dtype='U5')
color[:] = 'green'
color[rise] = 'white'
ecolor = np.zeros(rise.size, dtype='U5')
ecolor[:] = 'green'
ecolor[rise] = 'red'

plt.figure('AAPL')
plt.title('AAPL')
plt.xlabel('Date')
plt.ylabel('Closing Prise')
plt.grid(linestyle=':')
plt.plot(date, Close, zorder=3)
plt.plot(date, Open, zorder=3)
plt.bar(date, Close - Open, 0.8, Open, color=color, edgecolor=ecolor, zorder=3)
plt.vlines(date, low, high, color=ecolor)
plt.hlines(mean, date[0], date[-1], color='green', label='Mean')
plt.hlines(vwap, date[0], date[-1], label='Vwap', color='red')
plt.hlines(twap, date[0], date[-1], label='Twap', color='blue')
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()
