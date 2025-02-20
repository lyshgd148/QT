tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]
weight = 20
m = {(i, w): 0 for i in range(len(tr)) for w in range(weight + 1)}

for i in range(1, len(tr)):
    for w in range(1, weight + 1):
        if tr[i]['w'] > w:
            m[(i, w)] = m[(i - 1, w)]
        else:
            m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - tr[i]['w'])] + tr[i]['v'])

for i in range(len(tr)):
    for w in range(weight + 1):
        print(m[(i, w)], end=" ")
    print("\n")
