import matplotlib.pyplot as mp
import numpy as np

# 散点图
n = 300
x = np.random.normal(175, 20, n)
y = np.random.normal(55, 25, n)
mp.figure('scatter', facecolor='lightgray')
mp.title('scatter')
# 根据离均值点的距离分配颜色 越小则越蓝 越大越红
d = np.sqrt((x - 175) ** 2 + (y - 55) ** 2)
mp.scatter(x, y, marker='o', s=30, label='persons1', c=d, cmap='jet')
# mp.scatter(x, y, marker='o', s=30, label='persons2', c=d, cmap='jet_r')
mp.legend()
mp.grid(linestyle=':')

mp.show()
