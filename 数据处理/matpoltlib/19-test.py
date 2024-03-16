import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mp

b_type = np.dtype([
    ('pos', float, 2),
    ('siz', float, 1),
    ('rat', float, 1),
    ('col', float, 4)])
n = 100
b = np.zeros(n, dtype=b_type)
print(b)
b['pos'] = np.random.uniform(0, 1, (n, 2))
b['siz'] = np.random.uniform(50, 70, n)
b['rat'] = np.random.uniform(8, 10, n)
b['col'] = np.random.uniform(0, 1, (n, 4))

fig = plt.figure('lys')
plt.xticks([])
plt.yticks([])
sc = plt.scatter(b['pos'][:, 0], b['pos'][:, 1], s=b['siz'], color=b['col'])


def new(picture):
    index = picture % 100
    b['pos'][index] = np.random.uniform(0, 1, (1, 2))
    b['siz'][index] = np.random.uniform(50, 70, 1)
    b['siz'] += b['rat']
    sc.set_sizes(b['siz'])
    sc.set_offsets(b['pos'])


ava = mp.FuncAnimation(fig, new, interval=30)
plt.show()
