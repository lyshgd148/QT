import matplotlib.pyplot as plt
import numpy as np
import ProcessMode as md

LF = md.LowPassFilter(20, 0.001)
data = np.arange(0, 10.01, 0.001)


def f(data):
    return np.sin(100 * data) + np.cos(data) + 1.5 * np.sin(20 * data)


y = f(data)
y_fliter = list()
for i in y:
    y_fliter.append(LF.filter(i))

plt.figure()
plt.plot(data, y)
plt.figure()
plt.plot(data, y_fliter)
plt.show()
