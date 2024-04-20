import random


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


rate = [0, 0, 0, 0, 0]

temp = list()
temp_num = []
for i in range(100):
    num = roulette(rate)
    temp.append(num)

for i in range(5):
    temp_num.append(temp.count(i))

print(temp)
print(temp_num)
