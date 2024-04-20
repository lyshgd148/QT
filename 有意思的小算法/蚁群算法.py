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


rate = [0.2, 0.1, 0.2, 0.4, 0.1]

temp = list()
temp_num = []
for i in range(100000):
    num = roulette(rate)
    temp.append(num)

for i in range(5):
    temp_num.append(temp.count(i))

print(temp)
print(temp_num)
