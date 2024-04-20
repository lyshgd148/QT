import random

data = [[0, 2.7, 3.5, 4.8, 3.5],
        [2.7, 0, 2.7, 5.6, 5.5],
        [3.5, 2.7, 0, 3.1, 4.2],
        [4.8, 5.6, 3.1, 0, 2.7],
        [3.5, 5.5, 4.2, 2.7, 0]]

sign_density = [[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0]]
num_ants = 8

rou_p = 0.3
Q = 10
a = 1
b = 5


def roulette(rate):
    rand_num = random.random()
    rate_new = list()
    index = 0
    test = rate[0]
    rate_new.append(rate[0])
    for i in range(1, len(rate)):
        test += rate[i]
        rate_new.append(test)
    for i, j in enumerate(rate_new):
        if rand_num <= j:
            index = i
            break
    return index


def walk(i, table):  # table 放自己所在位置 以及走过的索引
    data_new = data[i]
    sign_density_new = sign_density[i]
    p = list()
    num = 0
    for j in range(len(data_new)):
        if j not in table:
            num += (((1 / data_new[j]) ** b) * (sign_density_new[j] ** a))
    for j in range(len(data_new)):
        if j not in table:
            p.append((((1 / data_new[j]) ** b) * (sign_density_new[j] ** a)) / num)
        else:
            p.append(0)
    index = roulette(p)
    return index
