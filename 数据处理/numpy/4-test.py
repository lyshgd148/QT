import numpy as np

# 变维
# 视图变维度（数据共享）
ary = np.arange(1, 10)
ary1 = ary.reshape(3, 3)
ary1[0] = 987
print(ary, 'ary')
print(ary1, 'ary1')
ary2 = ary1.flatten()
print(ary2)

print("*" * 60)
# 复制变维度（数据独立）
ary3 = ary.flatten()
ary3[0] = 1090291
print(ary)
print(ary3, 'ary3')
print("*" * 60)
# 就地变维 (不要返回值来得到改变的东西，本身就会改变)
ary.shape = (3, 3)
print(ary)
ary.resize((9,))
print(ary)
