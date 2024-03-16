import numpy as np
from scipy.signal import convolve2d
import pygame


class LifeGame:
    def __init__(self, speed):
        self.kernel = np.array([[1, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]])
        self.lifes = np.random.randint(0, 2, (80, 80))
        size = (801, 801)
        self.done = False
        # 初始化
        pygame.init()
        self.screen = pygame.display.set_mode(size, flags=pygame.NOFRAME)
        # 创建时钟对象
        self.clock = pygame.time.Clock()
        self.speed = speed
        self.page_information()

    def refresh(self, life):
        lifes_next = convolve2d(life, self.kernel, 'same')
        mask1 = (lifes_next == 2)
        mask2 = (lifes_next == 3)
        mask3 = (life == 1)
        mask4 = (life == 0)
        lifes_next[(mask3 & (mask1 | mask2)) | (mask4 & mask2)] = 1  # 这就是逻辑的力量 或者说是掩码的力量 哈哈哈！
        lifes_next[~((mask3 & (mask1 | mask2)) | (mask4 & mask2))] = 0
        return lifes_next

    def mesh_grid(self, Screen):
        for i in range(81):
            pygame.draw.line(Screen, (155, 155, 155), [i * 10, 0], [i * 10, 800], width=1)
        for i in range(81):
            pygame.draw.line(Screen, (155, 155, 155), [0, i * 10], [800, i * 10], width=1)

    def refresh_grid(self, num):
        indexs = np.where(num == 1)
        for i in range(len(indexs[0])):
            row, col = indexs[0][i], indexs[1][i]
            pygame.draw.rect(self.screen, (255, 255, 255), (row * 10 + 1, col * 10 + 1, 9, 9), 0)

    def page_information(self):
        flag = 0
        text0 = '''FBI警告⚠:按空格准备,然后按鼠标选点,之后按回车开始！'''
        f = pygame.font.SysFont(['microsoftyahei'], 25, False, False)
        text = f.render(text0, True, (220, 220, 220), (0, 0, 0))
        textRect = text.get_rect()
        # 设置显示对象居中
        textRect.center = (400, 350)
        self.screen.blit(text, textRect)
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_SPACE:
                    self.screen.fill((0, 0, 0))
                    self.mesh_grid(self.screen)
                    self.refresh_grid(self.lifes)
                    flag = 1
                elif key == pygame.K_RETURN and flag == 1:
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN and flag == 1:
                x, y = event.pos
                x, y = x // 10, y // 10
                self.lifes[x][y] = 1 if self.lifes[x][y] == 0 else 0
                self.screen.fill((0, 0, 0))
                self.mesh_grid(self.screen)
                self.refresh_grid(self.lifes)

            pygame.display.flip()

    def mian(self):
        while not self.done:
            # 设置游戏的fps
            self.clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True  # 若检测到关闭窗口，则将done置为True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x, y = x // 10, y // 10
                    self.lifes[x][y] = 1 if self.lifes[x][y] == 0 else 0
                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_RETURN:
                        self.page_information()

            self.mesh_grid(self.screen)
            self.refresh_grid(self.lifes)
            self.lifes = self.refresh(self.lifes)
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
        # 点击关闭，退出pygame程序
        pygame.quit()


if __name__ == '__main__':
    game = LifeGame(8)
    game.mian()
