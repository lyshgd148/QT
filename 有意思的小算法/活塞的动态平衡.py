from scipy.optimize import fsolve
import matplotlib.pyplot as plt

t = [x * 0.01 for x in range(7601)]
solutions = []
solutions_height = []


def equation(x, t):
    return -x ** 3 + 55 * x ** 2 - 1000 * x + 6000 - t ** 2


for i in t:
    result = fsolve(equation, 15, args=(i,))
    solutions.append(result)

for k in solutions:
    solutions_height.append((15 - k) ** 0.5)

plt.figure()
plt.plot(t, solutions)
plt.plot(t, solutions_height)
plt.show()
