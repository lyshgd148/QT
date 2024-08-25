import matplotlib.pyplot as plt
import pandas as pd
import math

data = pd.read_excel('./GPS.xlsx')
r = 6357
width = list()
height = list()
x = list()
y = list()
z = list()

time = list(data[data.columns[0]])
latitude = list(data[data.columns[1]])  # 纬度
longitude = list(data[data.columns[2]])  # 经度
altitude = list(data[data.columns[3]])  # 海拔
print(len(latitude), len(longitude), len(altitude))


for i in range(len(time)):
    x.append(r * math.cos(math.radians(longitude[i])))
    y.append(r * math.sin(math.radians(longitude[i])))
    z.append(r * math.sin(math.radians(latitude[i])))

length=list()
for i in range(1,len(x)):
    cos_theta=(x[i]*x[i-1]+y[i]*y[i-1]+z[i]*z[i-1])/math.sqrt((x[i]**2+y[i]**2+z[i]**2)*(x[i-1]**2+y[i-1]**2+z[i-1]**2))

    length.append(math.sqrt(1-cos_theta**2)*r*1000)

print(length)