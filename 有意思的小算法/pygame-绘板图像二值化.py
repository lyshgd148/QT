import pygame
from pygame.locals import *
import cv2

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height), flags=pygame.NOFRAME)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
