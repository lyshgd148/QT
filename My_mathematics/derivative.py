import matplotlib.pyplot as plt


def derivative(fun, a, b, deta=0.001):
    x = list()
    y = list()
    d_y = list()
    for i in range(int((b - a) / deta)):
        x_, y_ = fun(deta * i + a)
        x.append(x_)
        y.append(y_)
        # print(y[i])

    for i in range(len(y) - 1):
        d_y.append((y[i + 1] - y[i]) / deta)
    d_y.append(d_y[-1])

    plt.plot(x, y, color='black')
    plt.plot(x, d_y, color='r')
    plt.show()


if __name__ == '__main__':
    def fun(x):
        x
        y = x ** 3 + 2 * x
        return x, y


    derivative(fun, 3, 12, 0.00001)
