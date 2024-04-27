def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    matrix_new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            matrix_new[j][i] = matrix[i][j]

    return matrix_new


if __name__ == '__main__':
    temp = transpose_matrix([[1, 2, 5], [3, 4, 6], [7, 8, 9]])
    print(temp)
