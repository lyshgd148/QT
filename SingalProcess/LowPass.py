import matplotlib.pyplot as plt
import numpy as np
import ProcessMode as md

md.LowPassFilter(1, 0.01)
data = np.arange(0, 10.01, 0.01)


def f(data):
    return np.sin(100 * data)


plt.figure()
plt.plot(data, f(data))
plt.show()
