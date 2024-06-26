import LU_decompose
import Transpose_matrix


def inverse_matrix(matrix):
    '''
    :param matrix: 输入的矩阵
    :return:矩阵的逆
    '''
    n = len(matrix)
    m = len(matrix[0])
    if n != m:
        raise ValueError('请输入一个方阵！')
    I = [[1 if i == j else 0 for i in range(n)] for j in range(m)]
    # I = [[row[i] for row in I] for i in range(m)]  # 单位阵的转置还是单位阵
    temp = list()
    for i in range(m):
        temp.append(LU_decompose.LU_decompose(matrix, I[i]))
    #
    matrix_new = Transpose_matrix.transpose_matrix(temp)
    return matrix_new


if __name__ == "__main__":
    # temp = LU_decompose.LU_decompose([[1, 2], [3, 4]], [0, 1])
    # print(temp)
    I = inverse_matrix([[1, 2, 4, 5], [3, 4, 5, 5], [7, 8, 5, 7], [8, 9, 5, 4]])
    for i in I:
        print(i)
