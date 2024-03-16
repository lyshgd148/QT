import numpy as np
import datetime as dt


def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%Y-%m-%d').date()
    wday = date.strftime("%A")
    return wday


date, Open, high, low, Close, volume = np.loadtxt('./AAPL.csv',
                                                  skiprows=1,
                                                  unpack=True,
                                                  delimiter=',',
                                                  usecols=[0, 1, 2, 3, 4, 6],
                                                  dtype='U10,f8,f8,f8,f8,f8',
                                                  converters={0: dmy2wday}
                                                  )
all_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
average_close = np.zeros(5)
for i, j in enumerate(all_data):
    average_close[i] = np.mean(Close[date == j])

print(average_close)
