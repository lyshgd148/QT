import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 100)
y1 = np.cos(x)
y = np.sin(x)
# 修改坐标轴
ax = mp.gca()  # 获取坐标轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 修改y刻度
mp.yticks([-1, -0.5, 0.5, 1])
# 修改x轴刻度
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
          [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$'])

# # 修改显示范围
# mp.xlim(0, np.pi)
# mp.ylim(0, 1)

# 显示图像
mp.plot(x, y1, linestyle='-', linewidth=1, alpha=0.7, label=r'$y1=cos(x)$')
mp.plot(x, y, label=r'$y=sin(x)$')

# 绘制特殊点
mp.scatter([x[60], x[60]], [y[60], y1[60]], marker='o', s=70, color='red', zorder=2, label='sample point')
# 为某个（些）点 添加说明
mp.annotate("[0,0]",
            xycoords='data',
            xy=(0, 0),
            textcoords='offset points',
            xytext=(20, -20),
            fontsize=10,
            arrowprops=dict(
                arrowstyle='->',
                connectionstyle='angle3')
            )

# 图例
mp.legend()
mp.show()
# with open('data.txt', 'w') as f:
#     f.write(str(x))
#     f.write('\n\n\n')
#     f.write(str(y1))
