import sqlite3

####这一段的代码用于将mysql数据库的 .sql文件数据（就是一堆sql语句） 转换成.db数据文件 这样好用sqlite3库来操作
# import re
#
# with open('city_table.sql', 'r') as f:
#     table = f.read()
# with open('city_data.sql', 'r') as f:
#     data = f.read()
# data = re.sub(r'network_test.city', 'city', data)
# data = data.split(';')
# data_ = list()
# for i in data:
#     if '\n' in i:
#         i = i.replace('\n', '')
#     if i:
#         i += ';'
#         data_.append(i)
#
# coon = sqlite3.connect('./data/city.db')
# c = coon.cursor()
# c.execute(table)
# for i in data_:
#     c.execute(i)
# coon.commit()
# coon.close()


coon = sqlite3.connect('./data/city.db')
c = coon.cursor()
distance_data = c.execute('''select * from city''')
distance_data = distance_data.fetchall()
coon.close()

distance_data = [list(row) for row in distance_data]

import random
import matplotlib.pyplot as plt


class Ants_alorithm:
    def __init__(self, data, sign_density, rou_p, Q, a, b, iter_num, num_ants):
        '''
        self, data, sign_density, rou_p, Q, a, b, iter_num, num_ants
        '''
        self.data = data
        self.sign_density = sign_density
        self.rou_p = rou_p
        self.Q = Q
        self.a = a
        self.b = b
        self.num_ants = num_ants
        self.iter_num = iter_num
        self.num = None
        self.way = None

    def roulette(self, rate):
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

    def inint_(self, num_ants):
        index = list()
        for i in range(num_ants):
            index.append(random.randint(0, 4))
        return index

    def walk(self, i, table):  # table 放自己所在位置 以及走过的索引 返回去往下一个地点的索引！ 只走一步！
        data_new = self.data[i]
        sign_density_new = self.sign_density[i]
        p = list()
        num = 0
        length = 0
        for j in range(len(data_new)):
            if j not in table:
                num += (((1 / data_new[j]) ** b) * (sign_density_new[j] ** a))
        for j in range(len(data_new)):
            if j not in table:
                p.append((((1 / data_new[j]) ** b) * (sign_density_new[j] ** a)) / num)
            else:
                p.append(0)
        index = self.roulette(p)
        length = self.data[i][index]
        return index, length

    def continue_walk(self, index):
        table = list()
        table.append(index)
        length = 0
        for i in range(len(self.data[0]) - 1):
            temp = self.walk(table[i], table)
            index = temp[0]
            table.append(index)
            length += temp[1]
        table.append(table[0])
        length += self.data[index][table[0]]
        return table, length

    def multi_continue_walk(self):  # num_ants 蚂蚁的数量
        num_ants_index = self.inint_(self.num_ants)
        table = list()
        length = list()
        for i in num_ants_index:
            temp = self.continue_walk(i)
            table.append(temp[0])
            length.append(temp[1])
        return table, length

    def renew_sign_density(self, table, length):
        row = len(self.sign_density)
        col = len(self.sign_density[0])
        deta_density = list()
        for i in range(row):
            for j in range(col):
                if i != j:
                    self.sign_density[i][j] = (1 - self.rou_p) * self.sign_density[i][j]

        for i in range(len(length)):
            deta_density.append(self.Q / length[i])

        for i in range(len(table)):
            for j in range(1, len(table[i])):
                self.sign_density[table[i][j - 1]][table[i][j]] += deta_density[i]
                self.sign_density[table[i][j]][table[i][j - 1]] += deta_density[i]

    def iterate(self, all_sum=0):
        all_sum += 1
        if all_sum <= self.iter_num:
            table, length = self.multi_continue_walk()
            self.renew_sign_density(table, length)
            if all_sum == 1:
                self.num = min(length)
                index = length.index(self.num)
                self.way = table[index]
            else:
                if self.num >= min(length):
                    self.num = min(length)
                    index = length.index(self.num)
                    self.way = table[index]
            return (self.iterate(all_sum))
        else:
            return self.num, self.way

    def main(self):
        print(self.iterate())


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(5000)  # 限制递归次数
    city = {0: 'NanJing', 1: 'WuXi', 2: 'XuZhou', 3: 'ChangZhou',
            4: 'SuZhou', 5: 'NanTong', 6: 'LianYunGang', 7: 'HuaiAn',
            8: 'YanCheng', 9: 'YangZhou', 10: 'ZhenJiang', 11: 'TaiZhou',
            12: 'SuQian'}
    coordinate = {0: (88, 109.7), 1: (100.8, 138.8), 2: (39.2, 80.8), 3: (93.6, 132.1),
                  4: (105.4, 143.9), 5: (90, 149.6), 6: (30, 117.7), 7: (54.3, 115.7),
                  8: (58.7, 135.7), 9: (80.7, 121.2), 10: (85.6, 121.7), 11: (97.1, 131.3),
                  12: (44.5, 99.7)}

    x = list()
    y = list()

    num_ants = 20
    rou_p = 0.3
    Q = 15
    a = 1
    b = 5
    iter_num = 1000
    sign_density = [[1 if i != j else 0 for j in range(len(distance_data[0]))] for i in range(len(distance_data))]
    ants = Ants_alorithm(distance_data, sign_density, rou_p, Q, a, b, iter_num, num_ants)
    ants.main()

    for i in ants.way:
        x.append(coordinate[i][1])
        y.append(108 - coordinate[i][0])
        print(city[i], end='->')
    for i in ants.way:
        plt.text(coordinate[i][1] - 1, 108 - coordinate[i][0] + 1, city[i], fontsize=8)

    ax = plt.gca()
    ax.set_aspect(1)
    plt.xlim(75, 155)
    plt.ylim(-5, 85)
    plt.scatter(x, y)
    for i in range(len(coordinate)):
        plt.plot(x[i:i + 2], y[i:i + 2])
        plt.pause(0.9)

    plt.show()
