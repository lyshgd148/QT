# list1 = list(range(10))
# list1 = int(list1) - 1
# print(list1)

# print([[0]*20]*2)


# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5]
# list1 += list2
#
# print(list1)
#


# a = ['a', 'b']
# b = 'dasdas'
# c = ','.join(a)
# print(c)
# d = c.split(',')
# print(d)

#
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from datetime import datetime
#
# # 创建日期数据
# dates = [
#     datetime(2022, 1, 1),
#     datetime(2022, 1, 2),
#     datetime(2022, 1, 3),
#     datetime(2022, 1, 4),
#     datetime(2022, 1, 5)
# ]
#
# # 创建对应的 y 值数据
# values = [1, 3, 2, 4, 5]
# # print(dates, type(dates[0]))
# # 绘制图形
# plt.plot(dates, values)
#
# # 格式化日期横坐标
# date_format = mdates.DateFormatter('%Y-%m-%d')
# plt.gca().xaxis.set_major_formatter(date_format)
# plt.gcf().autofmt_xdate()
#
# # 显示图形
# plt.show()

import numpy as np

ary1 = np.arange(1, 101)

ary2 = np.random.normal(50, 10, 100)

ary2[ary2 > ary1] = 0
print(ary2)
print(ary2.size)
