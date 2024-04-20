import random


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
    data = [[0, 10.7, 12, 9.7, 3.5],
            [10.7, 0, 3.8, 5.3, 13.7],
            [12, 3.8, 0, 3.1, 14.4],
            [9.7, 5.3, 3.1, 0, 11.9],
            [3.5, 13.7, 14.4, 11.9, 0]]

    sign_density = [[0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0]]
    num_ants = 8
    rou_p = 0.3
    Q = 10
    a = 1
    b = 5
    iter_num = 500

    ants = Ants_alorithm(data, sign_density, rou_p, Q, a, b, iter_num, num_ants)
    ants.main()
