import pygame
import sys
from itertools import count
from block import Block


SIZE = WIDTH, HEIGHT = 1200, 800
BLACK = 0, 0, 0
WHITE = 200, 200, 200
DIGITS = 5
TIME_STEPS = 20000
counter = count()

pygame.init()
screen = pygame.display.set_mode(SIZE)
FONT = pygame.font.SysFont("Times New Roman", 24)

block1 = Block(HEIGHT, 200, 20, 0, 1)
M2 = pow(100, DIGITS-1)
block2 = Block(HEIGHT, 500, 150, -1/(TIME_STEPS/2), M2)


while True:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, block1.prep_show())
    pygame.draw.rect(screen, WHITE, block2.prep_show())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for i in range(TIME_STEPS):
        if block1.collide(block2):
            v1 = block1.bounce(block2)
            v2 = block2.bounce(block1)
            block1.v = v1
            block2.v = v2
            next(counter)
        if block1.hit_wall():
            block1.reverse()
            next(counter)
        block1.update()
        block2.update()
    numeric_filter = filter(str.isdigit, str(counter))
    numeric_string = "".join(numeric_filter)
    font_render = FONT.render(numeric_string, 1, WHITE)
    screen.blit(font_render, (60, 60))
    pygame.display.flip()
