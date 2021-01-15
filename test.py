import pygame
from pygame.draw import *
from random import randint
#import sys
#import math

pygame.display.set_caption("Игра шарик")

size = width, height = 1280, 720
black = 0, 0, 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN]
Rad = randint(10, 50)

color = COLORS[randint(0, 3)]




def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    game_over = False
    smile_x = Rad
    smile_y = Rad
    dx = randint(1, 50)
    dy = randint(1, 50)





    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)
        smile_x += dx
        smile_y += dy

        if smile_y > height - Rad or smile_y < Rad:
            dy *= -1

        if smile_x > width - Rad or smile_x < Rad:
            dx *= -1


        circle (screen, color, (smile_x, smile_y), Rad)

        pygame.display.flip()
        pygame.time.wait(30)


if __name__ == '__main__':
    main()
    pygame.quit()
