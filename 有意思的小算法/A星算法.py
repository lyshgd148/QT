import copy
import matplotlib.pyplot as plt
import numpy as np


def a_star(map, start, goal, m, n):
    open_list = list()
    map_state = copy.deepcopy(map)
    way = list()
    map_state[start[0]][start[1]] = 2
    start_i = start[0]
    start_j = start[1]
    around = []
    flage = False
    while start_i != goal[0] or start_j != goal[1]:
        around.append((start_i, start_j))
        if start_i - 1 >= 0 and map_state[start_i - 1][start_j] != 2 and map[start_i - 1][start_j] != 1:
            g = abs(start_i - 1 - start[0]) + abs(start_j - start[1])
            h = abs(start_i - 1 - goal[0]) + abs(start_j - goal[1])
            open_list.append([start_i - 1, start_j, g, h, g + h])
            around.append((start_i - 1, start_j))
            map_state[start_i - 1][start_j] = 2

        if start_j - 1 >= 0 and map_state[start_i][start_j - 1] != 2 and map[start_i][start_j - 1] != 1:
            g = abs(start_i - start[0]) + abs(start_j - 1 - start[1])
            h = abs(start_i - goal[0]) + abs(start_j - 1 - goal[1])
            open_list.append([start_i, start_j - 1, g, h, g + h])
            around.append((start_i, start_j - 1))
            map_state[start_i][start_j - 1] = 2

        if start_j + 1 <= n - 1 and map_state[start_i][start_j + 1] != 2 and map[start_i][start_j + 1] != 1:
            g = abs(start_i - start[0]) + abs(start_j + 1 - start[1])
            h = abs(start_i - goal[0]) + abs(start_j + 1 - goal[1])
            open_list.append([start_i, start_j + 1, g, h, g + h])
            around.append((start_i, start_j + 1))
            map_state[start_i][start_j + 1] = 2

        if start_i + 1 <= m - 1 and map_state[start_i + 1][start_j] != 2 and map[start_i + 1][start_j] != 1:
            g = abs(start_i + 1 - start[0]) + abs(start_j - start[1])
            h = abs(start_i + 1 - goal[0]) + abs(start_j - goal[1])
            open_list.append([start_i + 1, start_j, g, h, g + h])
            around.append((start_i + 1, start_j))
            map_state[start_i + 1][start_j] = 2
        if not open_list:
            flage = True
            break
        min_index = min(range(len(open_list)), key=lambda i: open_list[i][4])
        temp = open_list.pop(min_index)
        start_i = temp[0]
        start_j = temp[1]
        way.append(around)
        around = []

    # 那么ok啦,回溯算法又可以进行简化了，倒序来进行 每循环一次后 删掉目标及目标后面的 及 切片操作！
    way = [row for row in way if len(row) > 1]
    route = list()
    route.append((goal[0], goal[1]))
    if flage:
        return []
    else:
        while way:
            new_goal = route[-1]
            for i in range(len(way)):
                of_list1 = way[len(way) - i - 1]
                of_list2 = of_list1[1:]
                if new_goal in of_list2:
                    route.append(of_list1[0])
                    way = way[:len(way) - i - 1]  # 加快运算
                    break

        route = route[::-1]
        return route


if __name__ == "__main__":
    map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]]
    m = len(map)
    n = len(map[0])
    temp = a_star(map, [1, 1], [m - 1, 14], m, n)

    o = list()
    oo = list()
    for i in range(m):
        for j in range(n):
            if map[i][j] == 0:
                o.append((i, j))
            else:
                oo.append((i, j))
    x_o = [i[1] for i in o]
    y_o = [m - 1 - i[0] for i in o]
    x_oo = [i[1] for i in oo]
    y_oo = [m - 1 - i[0] for i in oo]
    x = [i[1] for i in temp]
    y = [m - 1 - i[0] for i in temp]
    plt.scatter(x_o, y_o, facecolors='none', edgecolors='b', marker='o')
    plt.scatter(x_oo, y_oo, edgecolors='b', marker='o')
    plt.plot(x, y, color='r')
    ax = plt.gca()
    ax.set_aspect(1)
    plt.show()

# 实现了走迷宫的初步想法
