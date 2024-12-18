import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(t, u):
    x, y = u
    dxdt = ((x - t) / L ** 2) * (x - t + (y - np.log(1 + t)) / (1 + t))
    dydt = ((y - np.log(1 + t)) / L ** 2) * (x - t + (y - np.log(1 + t)) / (1 + t))
    dudt = [dxdt, dydt]
    return dudt


def inital(ang, l):
    return l * np.cos(ang), l * np.sin(ang)


L = 1
u0 = inital(np.pi, L)
t = np.linspace(0, 8, 10000)
front = np.log(1 + t)
sol = odeint(f, u0, t, tfirst=True)

plt.plot(sol[:, 0], sol[:, 1], color='r')

u0 = inital(np.pi * 5 / 4, L)
sol = odeint(f, u0, t, tfirst=True)
plt.plot(sol[:, 0], sol[:, 1], color='r')

u0 = inital(np.pi * 7 / 4, L)
sol = odeint(f, u0, t, tfirst=True)
plt.plot(sol[:, 0], sol[:, 1], color='r')

u0 = inital(np.pi / 2, L)
sol = odeint(f, u0, t, tfirst=True)
plt.plot(sol[:, 0], sol[:, 1], color='r')

u0 = inital(np.pi * 0, L)
sol = odeint(f, u0, t, tfirst=True)
plt.plot(sol[:, 0], sol[:, 1], color='r')

plt.plot(t, front, color='b')
plt.grid()
plt.show()
