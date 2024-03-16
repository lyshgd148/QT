# python 绘图的第一种实现方法 第二种见18-test.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 创建数据
x = np.linspace(0, 8 * np.pi, 400)
y = np.sin(x)
# 创建一个图形和轴
fig = plt.figure()
plt.ylim(-1, 1)
plt.xlim(0, 1)

# 控制绘制速度
v = 4


def update(frame):
    x_data = x[:frame * v]
    y_data = y[:frame * v]
    if frame > 1:
        plt.xlim(0, x_data[frame * v - 1] + 1)
    line.set_data(x_data, y_data)


# 创建一个空的线对象
line, = plt.plot([], [], lw=2) #用line, 是将列表拆包 虽然就一个元素（是个class生成的实例对象）
# print(list, len(line))
# print(line[0], type(line[0]))
# print(type(line))
# 创建动画对象
ani = FuncAnimation(fig, update, frames=int(len(x) / v), interval=50)
plt.show()
