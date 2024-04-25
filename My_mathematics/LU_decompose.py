def nzero(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if matrix[0][0] == 0 and n != 1:
        for i in range(1, n):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
                break
    if matrix[0][0] != 1:
        temp = matrix[0][0]
        for i in range(m):
            matrix[0][i] /= temp


def determinant(matrix):
    '''
    求一个方阵行列式的值
    (肯定是用递归来解决的，但是现在写不出来了,改天再写吧看，至少目前还不是刚需!)
    '''


def LU_decompose(coefficent, b):
    '''
    coefficent:系数矩阵
    b:等式右边的值 (是一个向量)
    此函数的作用是实现LU分解
    decompose 分解
    '''
    n = len(coefficent)
    m = len(coefficent[0])
    m += 1
    for i in range(n):  # 增广矩阵
        coefficent[i].append(b[i])

    for j in range(m - 2):
        temp = coefficent[j:]
        temp = [i[j:] for i in temp]
        for i in range(1, len(temp)):
            nzero(temp)
            k1 = temp[i][0]
            temp[i] = [temp[i][t1] - k1 * temp[0][t1] for t1 in range(len(temp[0]))]
        for k in range(n - j):
            coefficent[k + j] = []
            for t in range(j):
                coefficent[k + j].append(0)
            coefficent[k + j].extend(temp[k])

    if coefficent[-1][-2] == 0:
        raise ValueError('该线性方程组无唯一解')

    coefficent[-1][-2], coefficent[-1][-1] = 1, coefficent[-1][-1] / coefficent[-1][-2]
    for i in range(n - 1):
        for t in range(n - 1 - i):
            k2 = coefficent[n - 2 - i - t][m - 2 - i]
            coefficent[n - 2 - i - t] = [coefficent[n - 2 - i - t][num] - k2 * coefficent[n - 1 - i][num] for num in
                                         range(m)]
    temp = list()
    for i in coefficent:
        temp.append(i[-1])
    return temp


if __name__ == "__main__":
    temp = LU_decompose([[1, 2, 3], [2, 3, 4], [5, 7, 6]], [1, 2, 3])
    print(temp)
    temp = LU_decompose([[1, 0], [0, 2]], [1, 2])
    print(temp)

    # determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # matrix = [[0, 1, 2, 3], [2, 2, 3, 5], [3, 2, 1.4]]
    # nzero(matrix)
    # print(matrix)
