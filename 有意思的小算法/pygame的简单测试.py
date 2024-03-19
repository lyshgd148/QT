# import sys
# import pygame
#
# # 使用pygame之前必须初始化
# pygame.init()
# # 设置主屏窗口
# screen = pygame.display.set_mode((500, 500))
# # 设置窗口的标题，即游戏名称
# pygame.display.set_caption('生命游戏')
#
#
# face=pygame.Surface((10,10),flags=pygame.HWSURFACE)
# face.fill(color='white')
# face1=pygame.Surface((10,10),flags=pygame.HWSURFACE)
# face1.fill(color='white')
#
# while True:
#     # 循环获取事件，监听事件状态
#     for event in pygame.event.get():
#         # 判断用户是否点了"X"关闭按钮,并执行if代码段
#         if event.type == pygame.QUIT:
#             # 卸载所有模块
#             pygame.quit()
#             # 终止程序，确保退出程序
#             sys.exit()
#     screen.blit(face,(0,0))
#     screen.blit(face1, (0, 10))
#     pygame.display.flip()  # 更新屏幕内容


# import pygame
# # 引入pygame中所有常量，比如 QUIT
# from pygame.locals import *
#
# pygame.init()
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption('生命游戏')
#
# image_surface = pygame.image.load("test.jpeg").convert()
# image_surface.fill((0, 0, 255), rect=(100, 100, 100, 50), special_flags=0)
# image_new = pygame.transform.scale(image_surface, (200, int(1080 * 200 / 1440)))
# # 对新生成的图像进行旋转至45度
# image_1 = pygame.transform.rotate(image_new, 45)
# # 使用rotozoom() 旋转 0 度，将图像缩小0.5倍
# image_2 = pygame.transform.rotozoom(image_1, 0, 0.5)
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#     # 将最后生成的image_2添加到显示屏幕上
#     screen.blit(image_new, (0, 0))
#     pygame.display.update()


# import pygame
#
# # 引入pygame中所有常量，比如 QUIT
#
# pygame.init()
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption('生命游戏')
# image_surface = pygame.image.load("test.jpeg").convert()
# image_new = pygame.transform.scale(image_surface, (200, int(1080 * 200 / 1440)))
# x = 0
# y = 0
# while True:
#     # 等待事件发生
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             exit()
#     # events=pygame.event.wait()
#     # if events.type == pygame.QUIT:
#     #     exit()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         y -= 1
#     if keys[pygame.K_DOWN]:
#         y += 1
#     if keys[pygame.K_RIGHT]:
#         x += 1
#     if keys[pygame.K_LEFT]:
#         x -= 1
#     screen.fill((0, 0, 0))
#     screen.blit(image_new, (x, y))
#     pygame.display.flip()  # 更新屏幕内


# import pygame
# from random import randint
#
# # 初始化程序
# pygame.init()
# screen = pygame.display.set_mode((600, 600))
# pygame.display.set_caption("c语言中文网")
# # 更新显示
# pygame.display.flip()
# while True:
#     # 等待事件发生
#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         exit("成功退出")
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         # pos 获取鼠标当前位置
#         print('鼠标按下', event.pos)
#         mx, my = event.pos
#         # 调用 pygame.draw 模块画圆
#         pygame.draw.circle(screen, (255, 255, 0), (mx, my), 8)
#         # 处理完，更新显示
#         pygame.display.update()
#     if event.type == pygame.MOUSEBUTTONUP:
#         print('鼠标弹起')
#         pass
#     if event.type == pygame.MOUSEMOTION:
#         print('鼠标移动')
#         mx, my = event.pos
#         # 随机生成 RGB 颜色值
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         pygame.draw.circle(screen, (r, g, b,), (mx, my), 8)
#         # 处理完，更新显示
#         pygame.display.update()


# import pygame
# import numpy as np
#
#
# def mesh_grid(Screen):
#     for i in range(81):
#         pygame.draw.line(Screen, (155, 155, 155), [i * 10, 0], [i * 10, 800], width=1)
#     for i in range(81):
#         pygame.draw.line(Screen, (155, 155, 155), [0, i * 10], [800, i * 10], width=1)
# def refresh_grid(num):
#     indexs=np.where(num==1)
#     for i in  range(len(indexs[0])):
#         row,col=indexs[0][i],indexs[1][i]
#         pygame.draw.rect(screen, (255, 255, 255), (row*10+1, col*10+1, 9, 9), 0)
#
# size = (801, 801)
# done = False
# # 初始化
# pygame.init()
# screen = pygame.display.set_mode(size, flags=pygame.NOFRAME)
# # 创建时钟对象
# clock = pygame.time.Clock()
# while not done:
#     # 设置游戏的fps
#     clock.tick(24)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True  # 若检测到关闭窗口，则将done置为True
#     mesh_grid(screen)
#     # 绘制一个灰色的矩形区域，以灰色填充区域
#
#
#     pygame.display.flip()
# # 点击关闭，退出pygame程序
# pygame.quit()
