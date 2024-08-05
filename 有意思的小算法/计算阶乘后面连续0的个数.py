def Num_zero(x):
    temp = list()
    ls = list()
    Number = 0
    flag = 1
    time = 0
    index = 0

    temp1 = list()
    ls1 = list()
    if x == 1:
        return 0
    for i in range(1, x + 1):
        ls.append(i)
        ls1.append(i % 10)
    temp.append(ls)
    temp1.append(ls1)
    ls = []
    ls1 = []

    while True:
        for i in range(0, len(temp[time]) - 1):
            index = 0
            first = temp1[time].pop(0)
            first_ = temp[time].pop(0)
            if not temp1[time]:
                break
            for j in temp1[time]:
                num = first * j
                if num % 10 == 0:
                    flag = 1
                    temp1[time].pop(index)
                    t = temp[time].pop(index)
                    num = first_ * t
                    while num % 10 == 0:
                        num /= 10
                        num = int(num)  # 我操，这个数据类型坑死我了，可恶的科学计数法自己去四舍五入去了！！！
                        Number += 1
                    ls.append(num)
                    ls1.append(num % 10)
                    break
                index += 1

        if flag == 0:
            break
        flag = 0
        temp.append(ls)
        temp1.append(ls1)
        ls = []
        ls1 = []
        time += 1
    return Number


num = Num_zero(25)
print(num)