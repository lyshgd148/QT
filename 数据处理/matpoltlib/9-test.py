import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8 * np.pi, 8000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2
mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=14)
mp.grid(linestyle=":")
mp.plot(x, sinx, label=r'$y=sin(x)$')
mp.plot(x, cosx, label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.fill_between(x, sinx, cosx, sinx > cosx, alpha=0.3)
mp.fill_between(x, sinx, cosx, sinx < cosx, alpha=0.3)
mp.legend()
mp.show()
