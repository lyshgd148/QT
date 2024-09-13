import time

t1 = time.time()
print(t1)
for i in range(10000000000):
    pass
t2 = time.time()
print((t2 - t1) / 60)
