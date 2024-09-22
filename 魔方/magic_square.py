import copy


class magicSquare:
    def __init__(self):
        # 定义魔方初始状态
        self.face = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.up = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.back = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.right = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        self.down = [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
        self.ways = ['F', 'R', 'f', 'r', 'U', 'B', 'u', 'b', 'D', 'L', 'l', 'd']

    def resert(self):
        # 还原魔方
        self.face = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.up = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.back = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.right = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        self.down = [[6, 6, 6], [6, 6, 6], [6, 6, 6]]

    def getCorner(self):
        # 正面向着自己，从顶面向下看：左下1，右下2，右上3，左上4，底面左下1，右下2，右上3，左上4
        self.corner = [
            [self.left[0][2], self.face[0][0], self.up[2][0]],
            [self.face[0][2], self.right[0][0], self.up[2][2]],
            [self.right[0][2], self.back[0][0], self.up[0][2]],
            [self.back[0][2], self.left[0][0], self.up[0][0]],
            [self.left[2][2], self.face[2][0], self.down[0][0]],
            [self.face[2][2], self.right[2][0], self.down[0][2]],
            [self.right[2][2], self.back[2][0], self.down[2][2]],
            [self.back[2][2], self.left[2][0], self.down[2][0]]
        ]

    def getColor(self):
        self.color = [self.face, self.left, self.up, self.back, self.right, self.down]

    def getEdge(self):
        """
        正面向着自己，从顶面向下看：第一个为上层和正面的棱块，逆时针旋转一圈数0123
        中层为正面和右面的棱块，逆时针旋转一圈数4567
        """
        self.edge = [
            [self.face[0][1], self.up[2][1]],
            [self.right[0][1], self.up[1][2]],
            [self.back[0][1], self.up[0][1]],
            [self.left[0][1], self.up[1][0]],
            [self.face[1][2], self.right[1][0]],
            [self.right[1][2], self.back[1][0]],
            [self.back[1][2], self.left[1][0]],
            [self.left[1][2], self.face[1][0]]
        ]

    def check(self):
        # 检查魔方是否还原
        for row in self.face:
            for colour in row:
                if colour != 1:
                    return False
        for row in self.back:
            for colour in row:
                if colour != 4:
                    return False
        for row in self.left:
            for colour in row:
                if colour != 2:
                    return False
        for row in self.right:
            for colour in row:
                if colour != 5:
                    return False
        for row in self.up:
            for colour in row:
                if colour != 3:
                    return False
        for row in self.down:
            for colour in row:
                if colour != 6:
                    return False
        return True

    def F(self):
        temp = copy.deepcopy(self.face)
        for i in range(3):
            for j in range(3):
                self.face[i][j] = temp[2 - j][i]
        temp = copy.deepcopy(self.up)
        for i in range(3):
            self.up[2][i] = self.left[2 - i][2]
        temp1 = copy.deepcopy(self.right)
        for i in range(3):
            self.right[i][0] = temp[2][i]
        temp = copy.deepcopy(self.down)
        for i in range(3):
            self.down[0][i] = temp1[2 - i][0]
        for i in range(3):
            self.left[i][2] = temp[0][i]

    def f(self):
        # 哈哈哈，我被自己的天才想法震惊住了! 反正不是在计算资源紧张的设备上运行的，就这样多算两遍吧，懒得写了
        for i in range(3):
            self.F()

    def U(self):
        temp = copy.deepcopy(self.up)
        for i in range(3):
            for j in range(3):
                self.up[i][j] = temp[2 - j][i]
        temp = copy.deepcopy(self.back)
        for i in range(3):
            self.back[0][i] = self.left[0][i]
        temp1 = copy.deepcopy(self.right)
        for i in range(3):
            self.right[0][i] = temp[0][i]
        temp = copy.deepcopy(self.face)
        for i in range(3):
            self.face[0][i] = temp1[0][i]
        for i in range(3):
            self.left[0][i] = temp[0][i]

    def u(self):
        for i in range(3):
            self.U()

    def D(self):
        temp = copy.deepcopy(self.down)
        for i in range(3):
            for j in range(3):
                self.down[i][j] = temp[2 - j][i]
        temp = copy.deepcopy(self.face)
        for i in range(3):
            self.face[2][i] = self.left[2][i]
        temp1 = copy.deepcopy(self.right)
        for i in range(3):
            self.right[2][i] = temp[2][i]
        temp = copy.deepcopy(self.back)
        for i in range(3):
            self.back[2][i] = temp1[2][i]
        for i in range(3):
            self.left[2][i] = temp[2][i]

    def d(self):
        for i in range(3):
            self.D()

    def B(self):
        temp = copy.deepcopy(self.back)
        for i in range(3):
            for j in range(3):
                self.back[i][j] = temp[2 - j][i]
        temp = copy.deepcopy(self.up)
        for i in range(3):
            self.up[0][i] = self.right[i][2]
        temp1 = copy.deepcopy(self.left)
        for i in range(3):
            self.left[i][0] = temp[0][2 - i]
        temp = copy.deepcopy(self.down)
        for i in range(3):
            self.down[2][i] = temp1[i][0]
        for i in range(3):
            self.right[i][2] = temp[2][2 - i]

    def b(self):
        for i in range(3):
            self.B()

    def L(self):
        temp = copy.deepcopy(self.left)
        for i in range(3):
            for j in range(3):
                self.left[i][j] = temp[2 - j][i]
        temp = copy.deepcopy(self.up)
        for i in range(3):
            self.up[i][0] = self.back[2 - i][2]
        temp1 = copy.deepcopy(self.face)
        for i in range(3):
            self.face[i][0] = temp[i][0]
        temp = copy.deepcopy(self.down)
        for i in range(3):
            self.down[i][0] = temp1[i][0]
        for i in range(3):
            self.back[i][2] = temp[2 - i][0]

    def l(self):
        for i in range(3):
            self.L()

    def R(self):
        temp = copy.deepcopy(self.right)
        for i in range(3):
            for j in range(3):
                self.right[i][j] = temp[2 - j][i]
        temp = copy.deepcopy(self.up)
        for i in range(3):
            self.up[i][2] = self.face[i][2]
        temp1 = copy.deepcopy(self.back)
        for i in range(3):
            self.back[i][0] = temp[2 - i][2]
        temp = copy.deepcopy(self.down)
        for i in range(3):
            self.down[i][2] = temp1[2 - i][0]
        for i in range(3):
            self.face[i][2] = temp[i][2]

    def r(self):
        for i in range(3):
            self.R()

    def turn(self, turns):
        for i in turns:
            if i == "F":
                self.F()
            elif i == "f":
                self.f()
            elif i == "U":
                self.U()
            elif i == "u":
                self.u()
            elif i == "D":
                self.D()
            elif i == "d":
                self.d()
            elif i == "B":
                self.B()
            elif i == "b":
                self.b()
            elif i == "R":
                self.R()
            elif i == "r":
                self.r()
            elif i == "L":
                self.L()
            elif i == "l":
                self.l()

    def inv_turn(self, turns):
        temp = list()
        for i in range(len(turns)):
            temp.append(turns[i].swapcase())
        self.turn(temp)

    def check_x(self, color, standard):
        # 检查顶面目标棱块是否为目标颜色
        num = 0
        if self.up[0][1] == color:
            num += 1
        if self.up[1][0] == color:
            num += 1
        if self.up[1][2] == color:
            num += 1
        if self.up[2][1] == color:
            num += 1
        if num == standard:
            return True
        else:
            return False

    def xcross(self, times, standard):
        global x_sign

        x_sign = self.check_x(6, standard)
        if x_sign == True or times == 4:
            return

        for i in self.ways:
            self.turn(i)
            self.xcross(times + 1, standard)
            if x_sign:
                return
            else:
                self.inv_turn(i)

    def Xcross(self):
        for i in range(2, 5):
            self.xcross(0, i)

    def reDown(self):
        # 让顶面十字回到底面
        while self.face[0][1] != self.face[1][1] or self.up[2][1] != self.down[1][1]:
            self.U()
        self.F()
        self.F()

        while self.left[0][1] != self.left[1][1] or self.up[1][0] != self.down[1][1]:
            self.U()
        self.L()
        self.L()

        while self.right[0][1] != self.right[1][1] or self.up[1][2] != self.down[1][1]:
            self.U()
        self.R()
        self.R()

        while self.back[0][1] != self.back[1][1] or self.up[0][1] != self.down[1][1]:
            self.U()
        self.B()
        self.B()

    def fourDCorner(self, ls, indexs, num):
        """
        :param indexs:不在此角处的可能值
        :para num:角号
        """
        self.getCorner()
        turns = [["F", "U", "f", "u"],
                 ["R", "U", "r", "u"],
                 ["B", "U", "b", "u"],
                 ["L", "U", "l", "u"]]
        jiaos = [[self.left[2][2], 2, self.down[0][0]],
                 [self.right[2][0], 5, self.down[0][2]],
                 [self.right[2][2], 5, self.down[2][2]],
                 [self.back[2][2], 4, self.down[2][0]]]

        print(self.corner)
        for index, value in enumerate(self.corner):
            if ls[0] in value and ls[1] in value and ls[2] in value:
                if index > 4:
                    index = index - 4
                    self.turn(turns[index])
                for j in range(len(indexs)):
                    if index == indexs[j]:
                        temp = index - num
                        if temp > 0:
                            for i in range(temp):
                                self.U()
                        else:
                            for i in range(abs(temp)):
                                self.u()
                        break
                while True:
                    if jiaos[num][0] == jiaos[num][1] and jiaos[num][2] == 6:
                        print("@")
                        break
                    else:
                        self.turn(turns[num])
                        print("*")

    def fullDown(self):
        # 将底面完全还原
        ls_ = [[1, 2, 6],
               [1, 5, 6],
               [4, 5, 6],
               [4, 2, 6]]
        indexs_ = [[1, 2, 3],
                   [0, 2, 3],
                   [0, 1, 3],
                   [0, 1, 2]]
        for i in range(4):
            self.fourDCorner(ls_[i], indexs_[i], i)

    def testRotate(self):
        dict = {1: "红", 2: "蓝", 3: "黄", 4: "橙", 5: "绿", 6: "白"}

        # #单面测试是没有问题的
        # self.L()

        # 连续转动
        self.turn(['F', 'R', 'f', 'r', 'U', "L", "D"])  # 我c你妈，这个有一个错了就得调半天！
        self.getColor()
        print(self.color)

        # 顶面十字的测试，目前没问题！
        # self.turn(self.ways)
        # self.turn(['F', 'U', 'd', 'd'])
        # self.Xcross()
        # self.reDown()
        # self.fullDown()

        print('\n', "-f" * 30, '\n')
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n")
            print(dict[self.face[i // 3][i % 3]], end=",")

        print('\n', "-l" * 30, '\n')
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n")
            print(dict[self.left[i // 3][i % 3]], end=",")

        print('\n', "-r" * 30, '\n')
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n")
            print(dict[self.right[i // 3][i % 3]], end=",")

        print('\n', "-u" * 30, '\n')
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n")
            print(dict[self.up[i // 3][i % 3]], end=",")

        print('\n', "-b" * 30, '\n')
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n")
            print(dict[self.back[i // 3][i % 3]], end=",")

        print('\n', "-d" * 30, '\n')
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("\n")
            print(dict[self.down[i // 3][i % 3]], end=",")


if __name__ == "__main__":
    m = magicSquare()
    m.testRotate()
