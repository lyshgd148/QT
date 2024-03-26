import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt

min_ = -50
max_ = 50
dis_x = np.linspace(min_, max_, 15)
dis_y = np.sinc(dis_x)

linear = si.interp1d(dis_x, dis_y, 'cubic')
lin_x = np.linspace(min_, max_, 200)
lin_y = linear(lin_x)
x = np.linspace(min_, max_, 1000)
plt.plot(x, np.sinc(x), color='red', label='orignal')
plt.scatter(dis_x, dis_y, color='green', label='orignal point')
plt.plot(lin_x, lin_y, color='orange', label='inter_value')
plt.legend()
plt.show()
