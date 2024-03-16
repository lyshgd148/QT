import matplotlib.pyplot as plt
import numpy as np

n = 1000
theta = np.linspace(0, 4 * np.pi, n)
r = np.sin(theta)
plt.figure('Polar')
plt.axes(projection='polar')
plt.title('Polar', fontsize=16)
plt.xlabel(r"$\theta$", fontsize=14)
plt.ylabel(r"$\rho$", fontsize=14)
plt.tick_params(labelsize=8)
plt.grid(linestyle=':')
plt.plot(theta, r)
plt.show()
