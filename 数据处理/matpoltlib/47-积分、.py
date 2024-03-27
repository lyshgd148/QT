import scipy.integrate as si


def f(x):
    return x ** 2 + x + 1


print(si.quad(f, -5, 5))
