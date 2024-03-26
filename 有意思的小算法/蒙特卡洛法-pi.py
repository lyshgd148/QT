import random


def my_pi(n):
    hits = 0
    for i in range(n):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x ** 2 + y ** 2 <= 1:
            hits += 1
    return 4 * (hits / n)


print(my_pi(10000000000))  # 太疯狂了，我用100亿个点，来估算圆周率！ result:
