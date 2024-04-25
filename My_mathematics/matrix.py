def matrix_mulitiplication(a, b):
    '''
    矩阵a 乘 矩阵b
    m:矩阵a的列
    n:矩阵b的行
    '''
    m1 = len(a)  # a行
    m = len(a[0])
    n1 = len(b[0])  # b列
    n = len(b)
    temp = [[0 for i in range(n1)] for j in range(m1)]
    num = 0
    if m != n:
        raise ValueError('矩阵不能相乘,请检查你输入的矩阵是否可以相乘!')
    else:
        for i in range(m1):
            for j in range(n1):
                for k in range(n):
                    num += a[i][k] * b[k][j]  # 哈哈哈 这里好有感觉呀 毕竟矩阵相乘的 乘法次数是 n^3 用三个for循环也是可以理解的事情
                temp[i][j] = num
                num = 0
        return temp


if __name__ == "__main__":
    temp = matrix_mulitiplication([[1, 2], [3, 4]], [[1, 0]])
    print(temp)
