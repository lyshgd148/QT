import pygame
from pygame.locals import *

pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height), flags=pygame.NOFRAME)


# 画点
def point(screen, radius, x, y, color=(255, 255, 255)):
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if i ** 2 + j ** 2 <= radius ** 2:
                screen.set_at((x + i, y + j), color)


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


Cuab(213, 314, 80)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
