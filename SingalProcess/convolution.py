def convolution(x: list, h: list) -> list:
    temp = []
    l_x, l_h = len(x), len(h)
    point = 0
    if l_x >= l_h:
        for i in range(l_x + l_h - 1):
            s = 0
            if i + 1 <= l_h:
                for j in range(i + 1):
                    s += (x[i - j] * h[j])
            elif i + 1 <= l_x:
                for j in range(l_h):
                    s += (x[i - j] * h[j])
            else:
                point += 1
                for j in range(l_h - point):
                    s += (x[l_x - j - 1] * h[point + j])
            temp.append(s)

    elif l_x < l_h:
        for i in range(l_x + l_h - 1):
            s = 0
            if i + 1 <= l_x:
                for j in range(i + 1):
                    s += (x[i - j] * h[j])
            else:
                point += 1
                for j in range(l_x):
                    s += (x[l_x - 1 - j] * h[point + j])
            temp.append(s)
    return temp


if __name__ == "__main__":
    import random

    # 复杂度 n**2 还行暂时能用
    x = [random.randint(-10, 10) for _ in range(10000)]
    h = [random.uniform(-1, 1) for _ in range(1000)]
    print(convolution(x, h))
