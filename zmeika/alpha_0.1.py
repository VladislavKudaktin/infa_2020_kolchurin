import pygame
from pygame.draw import *

pygame.init()

display_width = 1000   # ширина
display_height = 1000  # высота
display = pygame.display.set_mode((display_width, display_height))


clock = pygame.time.Clock()

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("'ZMEIKA'")


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

R = 1

usr_x1 = 403
usr_y1 = 404
usr_x2 = 94
usr_y2 = 94

make_jump = False

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (0, 255, 0)
        self.active_color = (0, 255, 0)

    def draw(self, x, y, action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, int(self.width / R), int(self.height / R)))

            if click[0] == 1 and action is not None:
                pygame.time.delay(300)
                action()

        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, int(self.width / R), int(self.height / R)))


def trans_w():
    global usr_y1
    usr_y1 = usr_y1 - 50
    rect(display, white, (usr_x1, usr_y1 + 50, usr_x2, usr_y2))
def trans_s():
    global  usr_y1
    usr_y1 = usr_y1 + 50
    rect(display, white, (usr_x1, usr_y1 - 50, usr_x2, usr_y2))
def trans_a():
    global usr_x1
    usr_x1 = usr_x1 - 50
    rect(display, white, (usr_x1 + 50, usr_y1 , usr_x2, usr_y2))
def trans_d():
    global usr_x1
    usr_x1 = usr_x1 + 50
    rect(display, white, (usr_x1 - 50, usr_y1 , usr_x2, usr_y2))

"""
def start():
    while True:
        one_cycle()
        pass
"""

def one_cycle():
    global make_jump
    quit_button = Button(100, 100)

    rect(display, green, (0, 0, 100, 1000))
    rect(display, green, (0, 0, 1000, 100))
    rect(display, green, (0, 900, 1000, 1000))
    rect(display, green, (900, 0, 1000, 1000))

    rect(display, white, (100, 100, 800, 800))
    fon = pygame.image.load(('setka.png'))
    display.blit(fon, (100, 100))


    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                trans_w()
                fon = pygame.image.load(('setka.png'))
                display.blit(fon, (100, 100))
            if keys[pygame.K_s]:
                trans_s()
                fon = pygame.image.load(('setka.png'))
                display.blit(fon, (100, 100))
            if keys[pygame.K_a]:
                trans_a()
                fon = pygame.image.load(('setka.png'))
                display.blit(fon, (100, 100))
            if keys[pygame.K_d]:
                trans_d()
                fon = pygame.image.load(('setka.png'))
                display.blit(fon, (100, 100))
        rect(display, red, (usr_x1, usr_y1, usr_x2, usr_y2))


        quit_button.draw(display_width / 1000, display_height / 1000, exit)

        exit_button = pygame.image.load('quit.png')
        display.blit(exit_button, (0, 0))

        strelka = pygame.image.load('strelkaa.png')
        display.blit(strelka, (100, 900))
        strelka = pygame.image.load('strelkad.png')
        display.blit(strelka, (300, 900))

        pygame.display.update()
        clock.tick(60)


#start()
one_cycle()
pygame.quit()
quit()
