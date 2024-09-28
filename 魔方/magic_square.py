import copy
import cv2
import numpy as np


class magicSquare:
    def __init__(self, color):
        # 定义魔方初始状态
        self.face = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.up = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.back = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.right = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        self.down = [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
        self.ways = ['F', 'R', 'f', 'r', 'U', 'B', 'u', 'b', 'D', 'L', 'l', 'd']
        self.dictR = {
            10: ["u", "f", "U", "F", "U", "R", "u", "r"],
            1: ["U", "R", "u", "r", "u", "f", "U", "F"],
            20: ["u", "r", "U", "R", "U", "B", "u", "b"],
            2: ["U", "B", "u", "b", "u", "r", "U", "R"],
            30: ["u", "b", "U", "B", "U", "L", "u", "l"],
            3: ["U", "L", "u", "l", "u", "b", "U", "B"],
            40: ["u", "l", "U", "L", "U", "F", "u", "f"],
            4: ["U", "F", "u", "f", "u", "l", "U", "L"]
        }  # 旋转字典 哈哈哈，旋转字典字只不过是数学上的映射函数，如果写一个映射 字典可以少些一半 2:以5号为正面旋转
        self.lencolor = [[1, 5],
                         [5, 4],
                         [4, 2],
                         [2, 1]]  # 正确时棱的颜色
        self.method = []
        self.color = color

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
        self.method.append("F")

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
        self.method.append("U")

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
        self.method.append("D")

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
        self.method.append("B")

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
        self.method.append("L")

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
        self.method.append("R")

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

    def CheakAll(self):
        num = 0
        self.getColor()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if self.color[i][j][k] == self.color[i][1][1]:
                        num += 1
        if num == 54:
            return True
        else:
            return False

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
        if x_sign == True or times == 6:
            return

        for i in self.ways:
            self.turn(i)
            self.xcross(times + 1, standard)
            if x_sign:
                return
            else:
                self.inv_turn(i)

    def Xcross(self):
        if self.CheakAll():
            return
        for i in range(2, 5):
            self.xcross(0, i)

    def reDown(self):
        # 让顶面十字回到底面          （#这里可优化）
        if self.CheakAll():
            return
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
        jiaos = [[self.face[2][0], 1, self.down[0][0]],
                 [self.face[2][2], 1, self.down[0][2]],
                 [self.right[2][2], 5, self.down[2][2]],
                 [self.left[2][0], 2, self.down[2][0]]]

        for index, value in enumerate(self.corner):
            if ls[0] in value and ls[1] in value and ls[2] in value:
                if index >= 4:
                    index = index - 4
                    self.turn(turns[index])
                for j in range(len(indexs)):
                    if index == indexs[j]:
                        temp = index - num
                        if temp > 0:
                            for _ in range(temp):
                                self.U()
                        elif temp < 0:
                            for _ in range(abs(temp)):
                                self.u()
                        break

                while True:
                    if jiaos[num][0] == jiaos[num][1] and jiaos[num][2] == 6:
                        break
                    else:
                        self.turn(turns[num])
                        jiaos = [[self.face[2][0], 1, self.down[0][0]],
                                 [self.face[2][2], 1, self.down[0][2]],
                                 [self.right[2][2], 5, self.down[2][2]],
                                 [self.left[2][0], 2, self.down[2][0]]]

    def fullDown(self):
        # 将底面完全还原
        if self.CheakAll():
            return
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

    def Upmeidel(self):
        # 顶面层转到中间层函数
        for i in range(4):  # 四个棱
            self.getEdge()
            for k, value in enumerate(self.edge):
                if k < 4 and self.lencolor[i][0] in value and self.lencolor[i][1] in value:
                    t = k - i
                    if t > 0:
                        for _ in range(t):
                            self.U()
                    elif t < 0:
                        for _ in range(abs(t)):
                            self.u()
                    if value[0] == self.lencolor[i][0]:  # 操写成  if value[0] == self.lencolor[0] 傻逼！
                        self.turn(self.dictR[i + 1])
                    else:
                        self.u()
                        self.turn(self.dictR[(i + 1) * 10])

    def midelDetection(self):
        # 中间层棱块。
        self.getEdge()
        for k, value in enumerate(self.edge):
            for i in range(4):
                if k == (4 + i) and (
                        (value[0] != self.lencolor[i][0]) or (value[1] != self.lencolor[i][1])):  # 我草你妈，这个or害我夜里四点到早上6点
                    temp = value
                    while not (self.up[1][1] in temp):
                        self.turn(self.dictR[i + 1])
                        self.getEdge()
                        temp = self.edge[k]

    def RemeideLay(self):
        # 我的想发是先将中间层的所有棱块不匹配的棱块 换到成顶面棱块
        if self.CheakAll():
            return
        self.Upmeidel()
        self.midelDetection()
        self.Upmeidel()

    def Upcross(self):
        if self.CheakAll():
            return
        turns = ['F', 'R', 'U', 'r', 'u', 'f']
        if self.check_x(self.up[1][1], 4):
            return
        for _ in range(4):
            if self.up[1][0] == self.up[1][1] and self.up[1][2] == self.up[1][1]:  # 顶面一字
                self.turn(turns)
                return
            if self.up[1][0] == self.up[1][1] and self.up[0][1] == self.up[1][1]:  # 顶面小拐弯
                for _ in range(2):
                    self.turn(turns)
                return
            self.U()
        else:
            for _ in range(2):
                self.turn(turns)
            self.U()
            self.turn(turns)

    def ReUp(self):
        # 恢复顶面
        if self.CheakAll():
            return
        num = 0
        turns = [["r", "u", "R", "u", "r", "u", "u", "R"],
                 ["F", "U", "f", "U", "F", "U", "U", "f"]]  # 小鱼1，小鱼2
        while True:
            for i in range(3):
                for j in range(3):
                    if self.up[i][j] == self.up[1][1]:
                        num += 1
            if num == 9:
                return

            if num == 5:
                for _ in range(4):
                    if self.left[0][0] == self.up[1][1] and self.left[0][2] == self.up[1][1]:
                        self.turn(turns[0])
                        break
                    self.U()  # self.turn(turns[0])

            if num == 6:
                for _ in range(4):
                    if self.up[0][0] == self.up[1][1] and self.face[0][0] == self.up[1][1]:
                        self.turn(turns[0])
                        break
                    elif self.up[0][0] == self.up[1][1] and self.left[0][2] == self.up[1][1]:
                        self.turn(turns[1])
                        break
                    self.U()

            if num == 7:
                for _ in range(4):
                    if self.back[0][2] == self.up[1][1]:
                        self.turn(turns[0])
                        break
                    self.U()
            num = 0

    def ChangeFace(self, turns, now):
        # 当改变正面时 F、B、U、D、L、R的对应映射
        temp = []
        ls = [["F", "B", "U", "D", "L", "R", "f", "b", "u", "d", "l", "r"],
              ["R", "L", "U", "D", "F", "B", "r", "l", "u", "d", "f", "b"],
              ["B", "F", "U", "D", "R", "L", "b", "f", "u", "d", "r", "l"],
              ["L", "R", "U", "D", "B", "F", "l", "r", "u", "d", "b", "f"]]
        for turn in turns:
            id = ls[0].index(turn)
            temp.append(ls[now][id])
        return temp

    def theLastSecond(self):
        # 倒数第二步骤，想不出名字了，暂且凑合一下！
        if self.CheakAll():
            return
        turns = ["R", "R", "F", "F", "r", "b", "R", "F", "F", "r", "B", "r"]  # L公式
        standard = [self.face, self.right, self.back, self.left]
        while True:
            clr = [[self.face[0][0], self.face[0][2]],
                   [self.right[0][0], self.right[0][2]],
                   [self.back[0][0], self.back[0][2]],
                   [self.left[0][0], self.left[0][2]]]  # 以红色为正面逆时针旋转
            num = 0
            ls = []
            for i in range(4):  # 判断同一条边角块同色的数量
                if clr[i][0] == clr[i][1]:
                    num += 1
                    ls.append(i)

            temp = []
            for j in range(len(ls)):  # 相同之后判断什么颜色
                for i in range(4):
                    if clr[ls[j]][0] == standard[i][1][1]:
                        temp.append(ls[j] - i)
                        break

            if num == 4:
                if temp[0] > 0:
                    for _ in range(temp[0]):
                        self.U()
                elif temp[0] < 0:
                    for _ in range(abs(temp[0])):
                        self.u()
                return

            elif num == 1:
                if temp[0] > 0:
                    for _ in range(temp[0]):
                        self.U()
                elif temp[0] < 0:
                    for _ in range(abs(temp[0])):
                        self.u()
                now = ls[0] - temp[0]  # 确定颜色位置
                now = now - 1  # 确定以那个面为旋转基准面
                if now < 0:
                    now = 3
                turn = self.ChangeFace(turns, now)
                self.turn(turn)

            elif num == 0:
                self.turn(turns)

    def FinalEnd(self):
        # 最后一步了
        if self.CheakAll():
            return
        turns = [["r", "u", "R", "u", "r", "u", "u", "R"],
                 ["F", "U", "f", "U", "F", "U", "U", "f"]]  # 小鱼1，小鱼2
        standard = [self.face, self.right, self.back, self.left]
        local = [[0, 0], [2, 0], [2, 2], [0, 2]]

        while True:
            num = 0
            fishLoacal = []
            temp = 0

            for i in range(4):
                if standard[i][0][0] == standard[i][1][1] and standard[i][0][1] == standard[i][1][1] and standard[i][0][
                    2] == standard[i][1][1]:
                    num += 1
                    temp = i

            if num == 4:
                return
            if num == 0:
                self.turn(turns[0])  # 任意来一份小鱼
                for i in range(0, 3, 2):
                    for j in range(0, 3, 2):
                        if self.up[i][j] == self.up[1][1]:
                            fishLoacal.append(i)
                            fishLoacal.append(j)
                for i in range(4):
                    if local[i] == fishLoacal:
                        if standard[i][0][0] == self.up[1][1]:
                            turn = self.ChangeFace(turns[0], i)
                            self.turn(turn)
                        else:
                            turn = self.ChangeFace(turns[1], i)
                            self.turn(turn)
                        break

            if num == 1:
                # 判断顺时针or逆时针
                if temp < 2:
                    temp1 = temp + 3
                    temp2 = temp + 2
                    if temp1 == 4:
                        temp1 = 0
                else:
                    temp1 = temp - 1
                    temp2 = temp - 2
                if standard[temp2][0][1] == standard[temp1][1][1]:  # 逆时针
                    turn = self.ChangeFace(turns[0], temp)
                    self.turn(turn)
                else:  # 顺时针
                    temp = temp - 1
                    if temp < 0:
                        temp = 3
                    turn = self.ChangeFace(turns[1], temp)
                    self.turn(turn)

                for i in range(0, 3, 2):
                    for j in range(0, 3, 2):
                        if self.up[i][j] == self.up[1][1]:
                            fishLoacal.append(i)
                            fishLoacal.append(j)
                for i in range(4):
                    if local[i] == fishLoacal:
                        if standard[i][0][0] == self.up[1][1]:
                            turn = self.ChangeFace(turns[0], i)
                            self.turn(turn)
                        else:
                            turn = self.ChangeFace(turns[1], i)
                            self.turn(turn)
                        break

    def simple(self):
        Ls = ["FFF", "BBB", "UUU", "DDD", "LLL", "RRR"]
        Ls1 = ["fff", "bbb", "uuu", "ddd", "lll", "rrr"]
        ls = ["f", "b", "u", "d", "l", "r"]
        ls1 = ["F", "B", "U", "D", "L", "R"]
        del_ = ["Ff", "fF", "Bb", "bB", "Uu", "uU", "Dd", "dD", "Ll", "lL", "Rr", "rR"]
        temp = "".join(self.method)
        for _ in range(10):
            while True:
                flag = False
                for i in range(len(ls)):
                    temp = temp.replace(Ls[i], ls[i])
                for i in Ls:
                    if i in temp:
                        flag = True
                if flag == False:
                    break
            while True:
                flag = False
                for i in del_:
                    temp = temp.replace(i, "")
                for i in del_:
                    if i in temp:
                        flag = True
                if flag == False:
                    break
            while True:
                flag = False
                for i in range(len(ls)):
                    temp = temp.replace(Ls1[i], ls1[i])
                for i in Ls:
                    if i in temp:
                        flag = True
                if flag == False:
                    break
            while True:
                flag = False
                for i in del_:
                    temp = temp.replace(i, "")
                for i in del_:
                    if i in temp:
                        flag = True
                if flag == False:
                    break

        self.method = []
        for i in temp:
            self.method.append(i)

    def testRotate(self):
        dict = {1: "红", 2: "蓝", 3: "黄", 4: "橙", 5: "绿", 6: "白"}
        tp = [self.face, self.left, self.up, self.back, self.right, self.down]
        st = ["f", "l", "u", "b", "r", "d"]
        conver = {"红": 1, "蓝": 2, "黄": 3, "橙": 4, "绿": 5, "白": 6}
        # self.turn(['F',"D","l"])  # 我c你妈，这个有一个错了就得调半天！

        color = self.color

        for i in range(6):
            for j in range(3):
                for k in range(3):
                    tp[i][j][k] = conver[color[i][j][k]]

        self.Xcross()
        print(1, end=" ")
        self.reDown()  # 回到底面
        print(2, end=" ")
        self.fullDown()  # 复原底面
        print(3, end=" ")
        self.RemeideLay()  # 拼好中间层
        print(4, end=" ")
        self.Upcross()  # 拼好顶面十字
        print(5, end=" ")
        self.ReUp()  # 恢复顶面
        print(6, end=" ")
        self.theLastSecond()  # 倒数第二步
        print(7, end=" ")
        self.FinalEnd()  # 哈哈最后一步了
        print(8)

        # 打印公式
        # self.method = self.method[3:]
        self.simple()
        print(f"Need:{len(self.method)} times!")
        for i in range(len(self.method)):
            if i % 10 == 0 and i != 0:
                print("\n")
            print(self.method[i], end=" ")

        for j in range(6):
            print('\n', f"-{st[j]}" * 30, '\n')
            for i in range(9):
                if i % 3 == 0 and i != 0:
                    print("\n")
                print(dict[tp[j][i // 3][i % 3]], end=",")


class GetColor:
    def __init__(self):
        self.path = ["./picture/1.jpg", "./picture/2.jpg", "./picture/3.jpg", "./picture/4.jpg", "./picture/5.jpg",
                     "./picture/6.jpg"]
        self.colors = []

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.image_copy = self.image.copy()
                cv2.rectangle(self.image_copy, (self.ix, self.iy), (x, y), (0, 255, 0), 2)
                cv2.imshow('image', self.image_copy)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.rectangle(self.image, (self.ix, self.iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', self.image)

            w, h = abs(self.ix - x), abs(self.iy - y)
            roi = self.image[min(self.iy, y):min(self.iy, y) + h, min(self.ix, x):min(self.ix, x) + w]
            roi = cv2.resize(roi, (300, 300))
            self.getColor(roi)
            cv2.imshow('ROI', roi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def getColor(self, imgOutput1):
        imgOutput1 = cv2.resize(imgOutput1, (300, 300))
        width, height = 300, 300  # 设定图片大小
        yellow_min = np.array([10, 200, 140])
        yellow_max = np.array([50, 255, 240])
        red_min = np.array([0, 150, 90])
        red_max = np.array([10, 255, 160])
        blue_min = np.array([100, 60, 40])
        blue_max = np.array([130, 255, 110])
        white_min = np.array([6, 7, 130])
        white_max = np.array([50, 40, 200])
        orange_min = np.array([0, 50, 170])
        orange_max = np.array([20, 255, 255])
        green_min = np.array([40, 130, 100])
        green_max = np.array([80, 255, 180])
        color = []

        for i in range(3):
            temp = []
            for j in range(3):
                y_start = i * width // 3
                y_end = (i + 1) * width // 3
                x_start = j * width // 3
                x_end = (j + 1) * width // 3
                pic = imgOutput1[y_start:y_end, x_start:x_end]
                hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
                mask_red = cv2.inRange(hsv, red_min, red_max)
                red_bili = cv2.countNonZero(mask_red) / (pic.size / 3)
                mask_yellow = cv2.inRange(hsv, yellow_min, yellow_max)
                yellow_bili = cv2.countNonZero(mask_yellow) / (pic.size / 3)
                mask_blue = cv2.inRange(hsv, blue_min, blue_max)
                blue_bili = cv2.countNonZero(mask_blue) / (pic.size / 3)
                mask_white = cv2.inRange(hsv, white_min, white_max)
                white_bili = cv2.countNonZero(mask_white) / (pic.size / 3)
                mask_orange = cv2.inRange(hsv, orange_min, orange_max)
                orange_bili = cv2.countNonZero(mask_orange) / (pic.size / 3)
                mask_green = cv2.inRange(hsv, green_min, green_max)
                green_bili = cv2.countNonZero(mask_green) / (pic.size / 3)
                if red_bili >= 0.2:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:红")
                    temp.append("红")
                elif yellow_bili >= 0.2:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:黄")
                    temp.append("黄")
                elif blue_bili >= 0.2:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:蓝")
                    temp.append("蓝")
                elif white_bili >= 0.2:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:白")
                    temp.append("白")
                elif orange_bili >= 0.2:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:橙")
                    temp.append("橙")
                elif green_bili >= 0.2:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:绿")
                    temp.append("绿")
                else:
                    print(f"第{self.k + 1}张图第" + str(3 * i + j + 1) + "个格子:空")
                    temp.append("空")
            color.append(temp)
        self.colors.append(color)

    def Oneprocess(self, path):
        self.drawing = False
        self.ix, self.iy = -1, -1
        self.image = cv2.imread(path)
        self.image = cv2.resize(self.image, (self.image.shape[1] // 2, self.image.shape[0] // 2))
        self.image_copy = self.image.copy()
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw_rectangle)

        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        for k in range(6):
            self.k = k
            self.Oneprocess(self.path[k])
        return self.colors


if __name__ == "__main__":
    color = GetColor().run()
    magicSquare(color).testRotate()
