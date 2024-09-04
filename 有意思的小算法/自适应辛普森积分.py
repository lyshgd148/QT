import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(10000000)


def f(x):
    return np.sin(x)


def sample(f, a, b):
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) * 0.5) + f(b))


def simpson(f, a, b, n=1000):
    step = (b - a) / n
    result = 0
    for i in range(n):
        new_a = a + i * step
        new_b = new_a + step
        result += sample(f, new_a, new_b)
    return result


def adaptive_simpson(f, a, b, eps, current):
    mid = (a + b) / 2
    left_value = sample(f, a, mid)
    right_value = sample(f, mid, b)

    if abs(left_value + right_value - current) < eps:  # 如果达到要求
        return current
    else:
        return (adaptive_simpson(f, a, mid, eps * 0.5, left_value) + adaptive_simpson(f, mid, b, eps * 0.5,
                                                                                      right_value))


def draw(f, a, b, result):
    n = int(np.abs(b - a) / 0.01)
    x = np.linspace(a, b, n)
    y = f(x)
    plt.plot(x, y)
    plt.fill_between(x, y, color='skyblue', alpha=0.4)
    plt.text(x[len(x) // 3], y[len(y) // 2] * 0.5, f'area:{result}', fontsize=12, color='black')
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    a, b = 0, 2 / 3 * np.pi
    result = adaptive_simpson(f, a, b, 0.0001, sample(f, a, b))
    draw(f, a, b, result)
    print(result)
