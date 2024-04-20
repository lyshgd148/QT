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
    '''
    轮盘赌算法
    '''
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


def inint_(num_ants):
    index = list()
    for i in range(num_ants):
        index.append(random.randint(0, 4))
    return index


def walk(i, table):  # table 放自己所在位置 以及走过的索引 返回去往下一个地点的索引！ 只走一步！
    data_new = data[i]
    sign_density_new = sign_density[i]
    p = list()
    num = 0
    length = 0
    for j in range(len(data_new)):
        if j not in table:
            num += (((1 / data_new[j]) ** b) * (sign_density_new[j] ** a))
    for j in range(len(data_new)):
        if j not in table:
            p.append((((1 / data_new[j]) ** b) * (sign_density_new[j] ** a)) / num)
        else:
            p.append(0)
    index = roulette(p)
    length = data[i][index]
    return index, length


def continue_walk(index):
    table = list()
    table.append(index)
    length = 0
    for i in range(len(data[0]) - 1):
        temp = walk(table[i], table)
        index = temp[0]
        table.append(index)
        length += temp[1]
    table.append(table[0])
    length += data[index][table[0]]
    # print(table, length)
    return table, length


def multi_continue_walk(num_ants):  # num_ants 蚂蚁的数量
    num_ants_index = inint_(num_ants)
    table = list()
    length = list()
    for i in num_ants_index:
        temp = continue_walk(i)
        table.append(temp[0])
        length.append(temp[1])
    return table, length


# multi_continue_walk(num_ants)
def renew_rou():
    pass
