import pygame
from pygame.locals import *
import numpy as np
import math

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height), flags=pygame.NOFRAME)
running = True


# 这一步还可以进一步优化，我要重新一个这个方法，目前我只用一个像素，
# 这个放法优化的话，我想选者打表，表中没有的话在进行计算，这样会大大提高效率！
# 画点
def point(screen, radius, x, y, color=(255, 255, 255)):
    temp = radius  # 哈哈，有一点写代码的逻辑在里面了！
    screen.set_at((x, y), color)
    screen.set_at((x + 1, y), color)
    screen.set_at((x - 1, y), color)
    screen.set_at((x, y + 1), color)
    screen.set_at((x, y - 1), color)


# def point(screen, radius, x, y, color=(255, 255, 255)):
#     for i in range(-radius, radius + 1):
#         for j in range(-radius, radius + 1):
#             if i ** 2 + j ** 2 <= radius ** 2:
#                 screen.set_at((x + i, y + j), color)


# 画线
def line(screen, list_start_end):  # bug修复:两点重合
    '''
    :param list_start_end: 起点坐标，终点坐标
    '''
    x = int(list_start_end[0])
    y = int(list_start_end[1])
    x_e = int(list_start_end[2])
    y_e = int(list_start_end[3])
    if x == y and x_e == y_e:
        return

    if abs(x_e - x) >= abs(y_e - y):
        if x_e - x > 0:
            for i in range(x_e - x + 1):
                point(screen, 1, x + i, y + int(((y_e - y) / (x_e - x)) * i))
        elif x_e - x < 0:
            for i in range(0, x_e - x - 1, -1):
                point(screen, 1, x + i, y + int(((y_e - y) / (x_e - x)) * i))
        else:
            if y_e - y > 0:
                for i in range(y_e - y + 1):
                    point(screen, 1, x, y + i)
            elif y_e - y < 0:
                for i in range(0, y_e - y - 1, -1):
                    point(screen, 1, x, y + i)
    else:
        if y_e - y > 0:
            for i in range(y_e - y + 1):
                point(screen, 1, x + int(((x_e - x) / (y_e - y)) * i), y + i)
        elif y_e - y < 0:
            for i in range(0, y_e - y - 1, -1):
                point(screen, 1, x + int(((x_e - x) / (y_e - y)) * i), y + i)
        else:
            if x_e - x > 0:
                for i in range(abs(x_e - x) + 1):
                    point(screen, 1, x + i, y)
            elif x_e - x < 0:
                for i in range(0, x_e - x - 1, -1):
                    point(screen, 1, x + i, y)


# 画个立方体
def Cuab(x, y, w):
    line(screen, (x, y, x - w, y - w))
    line(screen, (x - w, y - w, x, y - 2 * w))
    line(screen, (x, y, x + w, y - w))
    line(screen, (x + w, y - w, x, y - 2 * w))

    line(screen, (x, y, x, y - w))
    line(screen, (x - w, y - w, x - w, y - 2 * w))
    line(screen, (x, y - 2 * w, x, y - 3 * w))
    line(screen, (x + w, y - w, x + w, y - 2 * w))

    line(screen, (x, y - w, x - w, y - 2 * w))
    line(screen, (x - w, y - 2 * w, x, y - 3 * w))
    line(screen, (x, y - 3 * w, x + w, y - 2 * w))
    line(screen, (x + w, y - 2 * w, x, y - w))


# 画圆
# 这一步的分段画法太漂亮了
def Circle(screen, r, x, y, color=(255, 255, 255)):
    if r > 0:
        for i in range(-int(r / 2), int(r / 2) + 1):
            y_temp = math.ceil(math.sqrt(r ** 2 - i ** 2))
            point(screen, 1, i + x, y + y_temp)
            point(screen, 1, i + x, y - y_temp, color)
        n = math.ceil(math.sqrt(r ** 2 - (r / 2) ** 2))
        for i in range(0, n + 1):
            x_temp = math.ceil(math.sqrt(r ** 2 - i ** 2))
            point(screen, 1, x + x_temp, y + i, color)
            point(screen, 1, x - x_temp, y + i, color)
            point(screen, 1, x + x_temp, y - i, color)
            point(screen, 1, x - x_temp, y - i, color)


cub_data = np.array([[-100, -100, 100, 100, -100, -100, 100, 100],
                     [-100, 100, -100, 100, -100, 100, -100, 100],
                     [100, 100, 100, 100, -100, -100, -100, -100],
                     [1, 1, 1, 1, 1, 1, 1, 1]])  # [x,y,z] 物体数据

# reduce_dimension = np.array([[1, 0, 0, 0],
#                              [0, 1, 0, 0],
#                              [0, 0, 0, 0],
#                              [0, 0, 0, 1]])  # 降维矩阵 (麻痹的扯淡，完全不需要 反而增加运算量！)


theta = 2 * (np.pi / 200)
a = 1  # 缩放系数
x_rot = 0
y_rot = 0
z_rot = 0


def scale_matrix(a):
    matrix = np.array([[a, 0, 0, 0],
                       [0, a, 0, 0],
                       [0, 0, a, 0],
                       [0, 0, 0, 1]])
    return matrix


# rot_x_matrix = np.array([[1, 0, 0, 0],
#                          [0, np.cos(x_rot), -np.sin(x_rot), 0],
#                          [0, np.sin(x_rot), np.cos(x_rot), 0],
#                          [0, 0, 0, 1]])
# rot_y_matrix = np.array([[np.cos(y_rot), 0, np.sin(y_rot), 0],
#                          [0, 1, 0, 0],
#                          [-np.sin(y_rot), 0, np.cos(y_rot), 0],
#                          [0, 0, 0, 1]])
# rot_z_matrix = np.array([[np.cos(z_rot), -np.sin(z_rot), 0, 0],
#                          [np.sin(z_rot), np.cos(z_rot), 0, 0],
#                          [0, 0, 1, 0],
#                          [0, 0, 0, 1]])


def rot_y_matrix(y_rot):
    matrix = np.array([[1, 0, 0, 0],
                       [0, np.cos(y_rot), -np.sin(y_rot), 0],
                       [0, np.sin(y_rot), np.cos(y_rot), 0],
                       [0, 0, 0, 1]])
    return matrix


def rot_x_matrix(x_rot):
    matrix = np.array([[np.cos(x_rot), 0, np.sin(x_rot), 0],
                       [0, 1, 0, 0],
                       [-np.sin(x_rot), 0, np.cos(x_rot), 0],
                       [0, 0, 0, 1]])
    return matrix


def rot_z_matrix(z_rot):
    matrix = np.array([[np.cos(z_rot), -np.sin(z_rot), 0, 0],
                       [np.sin(z_rot), np.cos(z_rot), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return matrix


def matrix_vector(matrix, vector):
    data = np.zeros((4, vector.shape[1]))
    for i in range(len(vector[0, :])):
        temp = np.dot(matrix, vector[:, i])
        data[:, i] = temp
    return data


def draw(matrix):
    matrix = matrix[:2, :]
    temp = [matrix[0][0] + 400, matrix[1][0] + 400, matrix[0][1] + 400, matrix[1][1] + 400]
    line(screen, temp)  # 1
    print('-')
    temp = [matrix[0][1] + 400, matrix[1][1] + 400, matrix[0][3] + 400, matrix[1][3] + 400]
    line(screen, temp)  # 2
    print('-')
    temp = [matrix[0][3] + 400, matrix[1][3] + 400, matrix[0][2] + 400, matrix[1][2] + 400]
    line(screen, temp)  # 3
    print('-')
    temp = [matrix[0][2] + 400, matrix[1][2] + 400, matrix[0][0] + 400, matrix[1][0] + 400]
    line(screen, temp)  # 4
    print('-')
    temp = [matrix[0][4] + 400, matrix[1][4] + 400, matrix[0][5] + 400, matrix[1][5] + 400]
    line(screen, temp)  # 5
    print('-')
    temp = [matrix[0][5] + 400, matrix[1][5] + 400, matrix[0][7] + 400, matrix[1][7] + 400]
    line(screen, temp)  # 6
    print('-')
    temp = [matrix[0][7] + 400, matrix[1][7] + 400, matrix[0][6] + 400, matrix[1][6] + 400]
    line(screen, temp)  # 7
    print('-')
    temp = [matrix[0][6] + 400, matrix[1][6] + 400, matrix[0][4] + 400, matrix[1][4] + 400]
    line(screen, temp)  # 8
    print('-')
    temp = [matrix[0][0] + 400, matrix[1][0] + 400, matrix[0][4] + 400, matrix[1][4] + 400]
    line(screen, temp)  # 9
    print('-')
    temp = [matrix[0][1] + 400, matrix[1][1] + 400, matrix[0][5] + 400, matrix[1][5] + 400]
    line(screen, temp)  # 10
    print('-')
    temp = [matrix[0][3] + 400, matrix[1][3] + 400, matrix[0][7] + 400, matrix[1][7] + 400]
    line(screen, temp)  # 11
    print('-')
    temp = [matrix[0][2] + 400, matrix[1][2] + 400, matrix[0][6] + 400, matrix[1][6] + 400]
    line(screen, temp)  # 12
    print('-')


draw(cub_data)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == K_UP:
                screen.fill((0, 0, 0))
                y_rot -= theta
                cub_data = matrix_vector(rot_y_matrix(y_rot), cub_data)
                draw(cub_data)
            elif key == K_DOWN:
                screen.fill((0, 0, 0))
                y_rot += theta
                cub_data = matrix_vector(rot_y_matrix(y_rot), cub_data)
                draw(cub_data)
            elif key == K_RIGHT:
                screen.fill((0, 0, 0))
                x_rot -= theta
                cub_data = matrix_vector(rot_x_matrix(x_rot), cub_data)
                draw(cub_data)
            elif key == K_LEFT:
                screen.fill((0, 0, 0))
                x_rot += theta
                cub_data = matrix_vector(rot_x_matrix(x_rot), cub_data)
                draw(cub_data)

            elif key == K_6:
                screen.fill((0, 0, 0))
                z_rot -= theta
                cub_data = matrix_vector(rot_z_matrix(z_rot), cub_data)
                draw(cub_data)
            elif key == K_4:
                screen.fill((0, 0, 0))
                z_rot += theta
                cub_data = matrix_vector(rot_z_matrix(z_rot), cub_data)
                draw(cub_data)

            elif key == K_7:
                screen.fill((0, 0, 0))
                a -= 0.1
                cub_data = matrix_vector(scale_matrix(a), cub_data)
                draw(cub_data)
            elif key == K_9:
                screen.fill((0, 0, 0))
                a += 0.1
                cub_data = matrix_vector(scale_matrix(a), cub_data)
                draw(cub_data)

        pygame.display.flip()

pygame.quit()

