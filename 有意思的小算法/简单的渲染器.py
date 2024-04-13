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
def line(screen, list_start_end):
    '''
    :param list_start_end: 起点坐标，终点坐标
    '''
    x = list_start_end[0]
    y = list_start_end[1]
    x_e = list_start_end[2]
    y_e = list_start_end[3]
    if abs(x_e - x) >= abs(y_e - y):
        if x_e - x >= 0:
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


cub_data = np.array([[-100, 100, -100, 100, -100, 100, -100, 100],
                     [-100, 100, -100, 100, -100, 100, -100, 100],
                     [100, 100, 100, 100, -100, -100, -100, -100],
                     [1, 1, 1, 1, 1, 1, 1, 1]])  # [x,y,z] 物体数据

reduce_dimension = np.array([[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 1]])  # 降维矩阵
a = 1  # 缩放系数
scale_matrix = np.array([[a, 0, 0, 0],
                         [0, a, 0, 0],
                         [0, 0, a, 0],
                         [0, 0, 0, 1]])  # 缩放矩阵

x_rot = 0
y_rot = 0
z_rot = 0
rot_x_matrix = np.array([[1, 0, 0, 0],
                         [0, np.cos(x_rot), -np.sin(x_rot), 0],
                         [0, np.sin(x_rot), np.cos(x_rot), 0],
                         [0, 0, 0, 1]])
rot_y_matrix = np.array([[np.cos(y_rot), 0, np.sin(y_rot), 0],
                         [0, 1, 0, 0],
                         [-np.sin(y_rot), 0, np.cos(y_rot), 0],
                         [0, 0, 0, 1]])
rot_z_matrix = np.array([[np.cos(z_rot), -np.sin(z_rot), 0, 0],
                         [np.sin(z_rot), np.cos(z_rot), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])


def matrix_vector(matrix, vector):
    data = np.zeros((4, vector.shape[1]))
    for i in range(len(vector[0, :])):
        temp = np.dot(matrix, vector[:, i])
        data[:, i] = temp
    return data



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
