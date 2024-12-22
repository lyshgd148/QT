import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tank_Battle_v1.0")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.display.flip()
    clock.tick(40)
pygame.quit()
