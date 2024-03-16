import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

# 矩阵式布局
for i in range(1, 17):
    mp.figure('sunplot', facecolor='lightgray')
    mp.subplot(4, 4, i)
    mp.text(0.5, 0.5, str(i), ha='center', va='center', size=26, alpha=0.5)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()

# 网格式布局（可以单元格合并）
mp.figure('Grid', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=26, alpha=0.5)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[0:2, 2:])
mp.text(0.5, 0.5, 2, ha='center', va='center', size=26, alpha=0.5)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[1:, :1])
mp.text(0.5, 0.5, 3, ha='center', va='center', size=26, alpha=0.5)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[2, 1:])
mp.text(0.5, 0.5, 4, ha='center', va='center', size=26, alpha=0.5)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, 5, ha='center', va='center', size=26, alpha=0.5)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

# 自由式布局
mp.figure('Flow layout', facecolor='lightgray')
mp.axes([0.05, 0.5, 0.9, 0.4])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=26, alpha=0.5)
mp.axes([0.05, 0.05, 0.5, 0.4])
mp.text(0.5, 0.5, 2, ha='center', va='center', size=26, alpha=0.5)
mp.show()
