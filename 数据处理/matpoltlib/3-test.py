import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 100)
y = np.cos(x)
y1 = np.sin(x)

mp.figure('A', facecolor='lightgray')
ax = mp.gca()  # 获取坐标轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# ax.spines['left'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', 0))
mp.plot(x, y, linestyle='-', linewidth=1, alpha=0.7, label=r'$y=cos(x)$')
mp.title('cos(x)', fontsize=15)
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.tight_layout()
mp.legend()

#
mp.figure('B', facecolor='lightgray')
ax = mp.gca()  # 获取坐标轴
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# ax.spines['left'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', 0))
mp.plot(x, y1, label=r'$y=sin(x)$')
mp.title('sin(x)', fontsize=15)
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.tight_layout()
mp.legend()
#
mp.show()
