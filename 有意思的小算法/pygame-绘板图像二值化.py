import pygame
from pygame.locals import *
import cv2
import numpy as np
from scipy.signal import convolve2d

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height), flags=pygame.NOFRAME)


# def point(screen, radius, x, y, color=(255, 255, 255)):
#     temp = radius  # 哈哈，有一点写代码的逻辑在里面了！
#     screen.set_at((x, y), color)
#     screen.set_at((x + 1, y), color)
#     screen.set_at((x - 1, y), color)
#     screen.set_at((x, y + 1), color)
#     screen.set_at((x, y - 1), color)


def gray2twoValue(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img[::2]
    img = img[:, ::2]
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])
    sobel_x = convolve2d(img, kernel_x, mode='same')
    sobel_y = convolve2d(img, kernel_y, mode='same')
    sobel_x = np.abs(sobel_x).astype(np.uint8)
    sobel_y = np.abs(sobel_y).astype(np.uint8)
    img = 0.5 * sobel_x + 0.5 * sobel_y
    img = img.astype(np.uint8)
    mask_high = ((img > 150) & (img <= 255))
    mask_low = (img <= 150)
    img[mask_high] = 255
    img[mask_low] = 0
    return img


def draw_picture(screen, x, y, img):
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            if img[i, j] != 0:
                screen.set_at((x + j, y + i), (255,255,255))
                # point(screen, 1, x + j, y + i, (255, 255, 255))


img = gray2twoValue("test.jpeg")
draw_picture(screen, 50, 80, img)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
