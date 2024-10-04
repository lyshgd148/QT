n = int(input())
h4cache = [None for _ in range(n + 1)]  # 高速缓存存储器


def hanluo4(n):
    if h4cache[n]:
        return h4cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        H = []
        for x in range(n):
            H.append(2 * hanluo4(x) + 2 ** (n - x) - 1)
        h4cache[n] = min(H)
    return h4cache[n]


print(hanluo4(n))
