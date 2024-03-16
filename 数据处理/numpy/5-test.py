import numpy as np

# 切片
ary = np.arange(1, 10)
print(ary[:])
print(ary[::])
print(ary[1:])
print(ary[0:-1])
print(ary[-1:-4:-1])
print(ary[:-1])
print(ary[::-1])
print(ary[::3])

print("&*" * 30)
ary.shape = (3, 3)
print(ary)
print(ary[:2, :2])
print(ary[:, ::2])
print("#$%" * 20)

# 掩码(打窟窿的穿带字纸片)
ary = np.arange(100)
ary1 = (ary % 3 == 0)
print(ary, 'ary')
print(ary1, 'ary1')
ary2 = ary[ary1]  # ary2掩码,基于bool
print(ary2, 'ary2')
ary3 = (ary % 3 == 0) & (ary % 7 == 0)
print(ary3, 'ary3')
print("*" * 60)
# 基于索引的掩码
phone = np.array(['Mate 60', 'Apple', 'Oppo', 'Vivo', 'mi'])
rank = [1, 0, 4, 2, 3]
print(phone[rank])
