import matplotlib.pyplot as plt
from struct_ import Queue


def hotPotato(num, step):
    q = Queue()
    for i in range(1, num + 1):
        q.enqueue(i)

    while q.size() > 1:
        for i in range(step - 1):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


# for i in range(1, 31):
#     print(hotPotato(i, 5), end=" | ")

def ditui(num):
    S = [1]
    start = 3
    for i in range(num):
        result = S[i] + 5
        start_new = start + 1
        if result <= start_new:
            S.append(result)
        else:
            S.append(result - start_new)
        start = start_new
    return S


print("\n")
# print(ditui(2000))

x = [3 + i for i in range(200001)]

plt.figure()
result = ditui(200000)
plt.plot(x, result)
plt.show()
