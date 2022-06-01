import pygame
import sys
from pygame.color import THECOLORS


pygame.init()
pygame.display.set_caption('MyGame')

FPS = 60
W = 1200
H = 800

x = W // 2
y = H - 150

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

background = pygame.image.load("bin/bg.png")
background = pygame.transform.scale(background, (W, H))


image = pygame.image.load("bin/1.png")
unit = pygame.transform.scale(image, (140, 100))
# screen.blit(unit, (W/2, 700))

while True:
    screen.blit(background, (0, 0))
    screen.blit(unit, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                x -= 30
            elif event.key == pygame.K_RIGHT:
                print("rigth")
                x += 30
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                print("up")

    pygame.display.update()
    clock.tick(FPS)

