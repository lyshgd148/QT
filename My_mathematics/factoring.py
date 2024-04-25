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

    matrix2 = list()
    for i in range(n2):
        temp = list()
        for j in range(len(result)):
            temp.append(denominator[i] * result[j])
        matrix2.append(temp)

    temp = list()
    temp = [0 for _ in range(n2 + len(result) - 1)]
    for k in range(n2 + len(result) - 1):
        for i in range(n2):
            for j in range(len(result)):
                if i + j == k:
                    temp[k] += matrix2[i][j]
    temp = temp[-n3:]
    numerator_new = numerator[-n3:]
    for i in range(n3):
        temp[i] = numerator_new[i] - temp[i]

    print('\n')
    string_num1 = 0
    string_num2 = 0
    for i in range(n1):
        if i != n1 - 1:
            if i == 0:
                if numerator[i] == 1:
                    s = f'x^{n1 - 1 - i}'
                    string_num1 += len(s)
                elif numerator[i] == -1:
                    s = f'-x^{n1 - 1 - i}'
                    string_num1 += len(s)
                else:
                    s = f'{numerator[i]}x^{n1 - 1 - i}'
                    string_num1 += len(s)

            if i != 0 and numerator[i] > 0:
                if numerator[i] == 1:
                    s = f'+x^{n1 - 1 - i}'
                    string_num1 += len(s)
                else:
                    s = f'+{numerator[i]}x^{n1 - 1 - i}'
                    string_num1 += len(s)
            elif i != 0 and numerator[i] < 0:
                if numerator[i] == -1:
                    s = f'-x^{n1 - 1 - i}'
                    string_num1 += len(s)
                else:
                    s = f'{numerator[i]}x^{n1 - 1 - i}'
                    string_num1 += len(s)
        else:
            if numerator[i] > 0:
                if numerator[i] == 1:
                    s = f'+x^{n1 - 1 - i}'
                    string_num1 += len(s)
                else:
                    s = f'+{numerator[i]}x^{n1 - 1 - i}'
                    string_num1 += len(s)
            elif numerator[i] < 0:
                if numerator[i] == -1:
                    s = f'-x^{n1 - 1 - i}'
                    string_num1 += len(s)
                else:
                    s = f'{numerator[i]}x^{n1 - 1 - i}'
                    string_num1 += len(s)
            s = " = "
            string_num1 += len(s)

    for i in range(len(result)):
        if i != len(result) - 1:
            if i == 0:
                if result[i] == 1:
                    s = f'x^{len(result) - 1 - i}'
                    string_num2 += len(s)
                elif result[i] == -1:
                    s = f'-x^{len(result) - 1 - i}'
                    string_num2 += len(s)
                else:
                    s = f'{result[i]}x^{len(result) - 1 - i}'
                    string_num2 += len(s)
            if i != 0 and result[i] > 0:
                if result[i] == 1:
                    s = f'+x^{len(result) - 1 - i}'
                    string_num2 += len(s)
                else:
                    s = f'+{result[i]}x^{len(result) - 1 - i}'
                    string_num2 += len(s)
            elif i != 0 and result[i] < 0:
                if result[i] == -1:
                    s = f'-x^{len(result) - 1 - i}'
                    string_num2 += len(s)
                else:
                    s = f'{result[i]}x^{len(result) - 1 - i}'
                    string_num2 += len(s)
        else:
            if result[i] > 0:
                if result[i] == 1:
                    s = f'+x^{len(result) - 1 - i}'
                    string_num2 += len(s)
                else:
                    s = f'+{result[i]}x^{len(result) - 1 - i}'
                    string_num2 += len(s)
            elif result[i] < 0:
                if result[i] == -1:
                    s = f'-x^{len(result) - 1 - i}'
                    string_num2 += len(s)
                else:
                    s = f'{result[i]}x^{len(result) - 1 - i}'
                    string_num2 += len(s)
            s = " + "
            string_num2 += len(s)

    for i in range(n1):
        if i != n1 - 1:
            if i == 0:
                if numerator[i] == 1:
                    print(f'x^{n1 - 1 - i}', end='')
                elif numerator[i] == -1:
                    print(f'-x^{n1 - 1 - i}', end='')
                else:
                    print(f'{numerator[i]}x^{n1 - 1 - i}', end='')

            if i != 0 and numerator[i] > 0:
                if numerator[i] == 1:
                    print(f'+x^{n1 - 1 - i}', end='')
                else:
                    print(f'+{numerator[i]}x^{n1 - 1 - i}', end='')
            elif i != 0 and numerator[i] < 0:
                if numerator[i] == -1:
                    print(f'-x^{n1 - 1 - i}', end='')
                else:
                    print(f'{numerator[i]}x^{n1 - 1 - i}', end='')
        else:
            if numerator[i] > 0:
                if numerator[i] == 1:
                    print(f'+x^{n1 - 1 - i}', end='')
                else:
                    print(f'+{numerator[i]}x^{n1 - 1 - i}', end='')
            elif numerator[i] < 0:
                if numerator[i] == -1:
                    print(f'-x^{n1 - 1 - i}', end='')
                else:
                    print(f'{numerator[i]}x^{n1 - 1 - i}', end='')
            print(" = ", end='')

    for i in range(len(result)):
        if i != len(result) - 1:
            if i == 0:
                if result[i] == 1:
                    print(f'x^{len(result) - 1 - i}', end='')
                elif result[i] == -1:
                    print(f'-x^{len(result) - 1 - i}', end='')
                else:
                    print(f'{result[i]}x^{len(result) - 1 - i}', end='')
            if i != 0 and result[i] > 0:
                if result[i] == 1:
                    print(f'+x^{len(result) - 1 - i}', end='')
                else:
                    print(f'+{result[i]}x^{len(result) - 1 - i}', end='')
            elif i != 0 and result[i] < 0:
                if result[i] == -1:
                    print(f'-x^{len(result) - 1 - i}', end='')
                else:
                    print(f'{result[i]}x^{len(result) - 1 - i}', end='')
        else:
            if result[i] > 0:
                if result[i] == 1:
                    print(f'+x^{len(result) - 1 - i}', end='')
                else:
                    print(f'+{result[i]}x^{len(result) - 1 - i}', end='')
            elif result[i] < 0:
                if result[i] == -1:
                    print(f'-x^{len(result) - 1 - i}', end='')
                else:
                    print(f'{result[i]}x^{len(result) - 1 - i}', end='')
            print(" + ", end='')

    print('\n')
    print(string_num1, string_num2)
    return result, temp


if __name__ == "__main__":
    temp = LU_decompose.LU_decompose([[1, 2, 3], [3, 2, 5], [4, 6, 7]], [2, 5, 1])
    print(temp)
    temp = factoring([1, -4, 6, -4, 1, 0, 0, 0, 0], [1, 0, 1])
    # print(temp)
