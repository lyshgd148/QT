# # 移动均线
# import numpy as np
#
# ary = np.random.randint(1, 100,100)
# aver = np.zeros(96)
# for i in range(ary.size - (5 - 1)):
#     i = i + 4
#     test_ary = ary[i - 4:i + 1]
#     aver[i-4] = np.mean(test_ary)
# print(aver)


import matplotlib.pyplot as plt
import numpy as np

# 5日均线
date, Open, high, low, Close = np.loadtxt('./AAPL.csv',
                                          skiprows=1,
                                          unpack=True,
                                          delimiter=',',
                                          usecols=[0, 1, 2, 3, 4],
                                          dtype='M8[D],f8,f8,f8,f8'
                                          )
ma5 = np.zeros(date.size - 4)
for i in range(ma5.size):
    ma5[i] = np.mean(Close[i:i + 5])
plt.plot(date[4:], ma5, label='MA-5')
plt.plot(date, Close, label='APPL')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
