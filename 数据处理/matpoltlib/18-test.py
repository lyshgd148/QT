# python绘图的第二种方法,其实高级一点的话可以考虑用 线程 来写
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 8 * np.pi, 400)
y = np.sin(x)
# 创建一个图形和轴
fig = plt.figure()
plt.ylim(-1, 1)
plt.xlim(0, 1)

plt.plot([], [], 'b')
frame = 0
while True:
    frame += 4
    plt.plot(x[:frame], y[:frame], 'b')
    plt.xlim(0, x[frame - 1] + 1)
    plt.pause(0.1)
    plt.cla()
    if frame >= len(x):
        frame = 0
# 哈哈哈 我觉得我的这个写法好简单呀,简直就是小天才,牛逼！！
