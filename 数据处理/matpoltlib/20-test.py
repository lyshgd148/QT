import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mp

fig = plt.figure('Signal')
x = 0


def upd(data):
    t, v = data
    x, y = pl.get_data()
    x = np.append(x, t)
    y = np.append(y, v)
    pl.set_data(x, y)
    if x[-1] > 10:
        plt.xlim(x[-1] - 10, x[-1])


def genrate():
    global x
    y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
    yield x, y
    x += 0.01


plt.xlim(0, 10)
plt.grid(linestyle=':', alpha=0.5)
pl, = plt.plot([], [], label='single')
plt.legend()
ava = mp.FuncAnimation(fig, upd, genrate,interval=10)

plt.show()


