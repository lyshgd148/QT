import LU_decompose


def factoring(numerator, denominator):
    '''
    numerator:分子
    denominator:分母
    '''
    n1 = len(numerator)
    n2 = len(denominator)
    if n1 < n2:
        return
    else:
        n = n1 - n2 + 1
    num = [1 for _ in range(n)]
    n3 = n2 - 1  # 要去除的数的数量
    matrix = list()
    for i in range(n2):
        temp = list()
        for j in range(len(num)):
            temp.append(denominator[i] * num[j])
        matrix.append(temp)

    matrix1 = list()
    for k in range(n2 + len(num) - 1):
        temp = list()
        temp = [0 for _ in range(len(num))]
        for i in range(n2):
            for j in range(len(num)):
                if i + j == k:
                    temp[j] = matrix[i][j]
        matrix1.append(temp)

    matrix1 = matrix1[0:len(matrix1) - n3]
    numerator_new = numerator[0:len(numerator) - n3]
    result = LU_decompose.LU_decompose(matrix1, numerator_new)

    return result


if __name__ == "__main__":
    temp = LU_decompose.LU_decompose([[1, 2, 3], [3, 2, 5], [4, 6, 7]], [2, 5, 1])
    print(temp)
    temp = factoring([3, 2, 2, 1, 3], [1, 0, 1])
    print(temp)
