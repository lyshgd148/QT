import matplotlib.pyplot as plt
import numpy as np

date, Open, high, low, close = np.loadtxt('./AAPL.csv',
                                          skiprows=1,
                                          unpack=True,
                                          delimiter=',',
                                          usecols=[0, 1, 2, 3, 4],
                                          dtype='M8[D],f8,f8,f8,f8'
                                          )
plt.figure('AAPL')
plt.title('AAPL')
plt.xlabel('Date')
plt.ylabel('Closing Prise')
plt.grid(linestyle=':')
plt.plot(date, close)
plt.gcf().autofmt_xdate()
plt.show()
