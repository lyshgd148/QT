import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(t, u):
    x, y = u
    dxdt = ((x - t) / L ** 2) * (x - t + 2 * t * y - 2 * t ** 3)
    dydt = ((y - t ** 2) / L ** 2) * (x - t + 2 * t * y - 2 * t ** 3)
    dudt = [dxdt, dydt]
    return dudt

L = 1
u0 = [-L, 0]
t = np.linspace(0, 10, 1000)
front = t ** 2
sol = odeint(f, u0, t, tfirst=True)

plt.plot(sol[:, 0], sol[:, 1], color='r')
plt.plot(t, front, color='b')
plt.grid()
plt.show()
