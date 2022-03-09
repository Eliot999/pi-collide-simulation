import pygame
import sys

from block import Block

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
screen = pygame.display.set_mode(SIZE)

block1 = Block(HEIGHT, 100, 20, 0)
block2 = Block(HEIGHT, 300, 150, -1)


while True:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (395, 0, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
