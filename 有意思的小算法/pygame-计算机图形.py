import time

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
            for i in range(abs(y_e - y) + 1):
                point(screen, 1, x, y + i * ((y_e - y) / abs(y_e - y)))
    else:
        if y_e - y > 0:
            for i in range(y_e - y + 1):
                point(screen, 1, x + int(((x_e - x) / (y_e - y)) * i), y + i)
        elif y_e - y < 0:
            for i in range(0, y_e - y - 1, -1):
                point(screen, 1, x + int(((x_e - x) / (y_e - y)) * i), y + i)
        else:
            for i in range(abs(x_e - x) + 1):
                point(screen, 1, x + i * ((x_e - x) / abs(x_e - x)), y)


for i in range(-150,151):
    line(screen, (300, 300, 150+i, 150))
    line(screen, (300, 300, 150 , 150+i))
    pygame.display.flip()

# for i in range(500):
#     point(screen,1,200 + i, 100 + i*3, (255, 0, 0))

# def circle(screen, x, y, r):
#     for i in range(-r, r + 1):
#         for j in range(-r, r + 1):
#             if i ** 2 + j ** 2 == r ** 2:
#                 point(screen, 1, x + i, y + j)
# for r in range(1,301):
#     circle(screen, 300, 300, r)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
