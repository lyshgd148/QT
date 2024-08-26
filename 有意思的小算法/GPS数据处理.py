import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import math

data = pd.read_excel('./GPS.xlsx')
r = 6357
width = [0]
height = [0]
x = list()
y = list()
z = list()

time = list(data[data.columns[0]])
latitude = list(data[data.columns[1]])  # 纬度
longitude = list(data[data.columns[2]])  # 经度
altitude = list(data[data.columns[3]])  # 海拔

for i in range(len(time)):
    x.append(r * math.cos(math.radians(longitude[i])))
    y.append(r * math.sin(math.radians(longitude[i])))
    z.append(r * math.sin(math.radians(latitude[i])))

x_ = list()
y_ = list()
long = 0
for i in range(1, len(x)):
    cos_theta = (x[i] * x[i - 1] + y[i] * y[i - 1] + z[i] * z[i - 1]) / math.sqrt(
        (x[i] ** 2 + y[i] ** 2 + z[i] ** 2) * (x[i - 1] ** 2 + y[i - 1] ** 2 + z[i - 1] ** 2))
    theta = math.acos(cos_theta)
    length = theta * r * 1000
    long += length
    l = math.sqrt((longitude[i] - longitude[i - 1]) ** 2 + (latitude[i] - latitude[i - 1]) ** 2)
    x_.append((longitude[i] - longitude[i - 1]) / l * length)
    y_.append((latitude[i] - latitude[i - 1]) / l * length)
    sum_x = 0
    sum_y = 1
    for k in range(i):
        sum_x += x_[k]
        sum_y += y_[k]
    width.append(sum_x)
    height.append(sum_y)


def draw(x, y, z, long):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.scatter(0, 0, 0, c='red', marker='o')
    ax.text(0, 0, 0, r'$\text{all distance:} %d$' % long, fontsize=12, color='green')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


draw(width, height, altitude, long)
