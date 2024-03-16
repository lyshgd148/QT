import numpy as np

data = [('lys1', [2, 3, 4], 20), ('lys2', [3, 4, 7], 21), ('lys3', [6, 8, 9], 22)]
ary = np.array(data, dtype='U5,3int32,int32')
print(ary)

ary = np.array(data, dtype=[('name', 'str_', 4),
                            ('score', 'int32', 3),
                            ('age', 'int32', 1)])  # 几个字段几个元组  别名，类型，数量
print(ary[1]['score'])

print("*" * 60)

ary = np.array(data, dtype={'names': ['name', 'score', 'age'],
                            'formats': ['U4', '3int32', 'uint8']})
print(ary[0]['score'])

print("*" * 60)
# numpy日期
data = ['2024-03-01 10:23:10', '2023-10-04 14:23', '2022-04-06 23', '2021-04-07', '2020-01']
ary = np.array(data)
ary = ary.astype('M8[D]')  # 转化为日期类型
print(ary)
print(ary[1] - ary[0])
