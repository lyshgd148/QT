import matplotlib.pyplot as plt
import numpy as np

# K线图
date, Open, high, low, close = np.loadtxt('./AAPL.csv',
                                          skiprows=1,
                                          unpack=True,
                                          delimiter=',',
                                          usecols=[0, 1, 2, 3, 4],
                                          dtype='M8[D],f8,f8,f8,f8'
                                          )
rise = close > Open
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
plt.plot(date, close, zorder=3)
plt.plot(date, Open, zorder=3)
plt.bar(date, close - Open, 0.8, Open, color=color, edgecolor=ecolor, zorder=3)
plt.vlines(date, low, high, color=ecolor)
plt.gcf().autofmt_xdate()
plt.show()
