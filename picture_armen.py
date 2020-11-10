import pygame
from pygame.draw import *

pygame.init()
#_________________________________________________________________________
FPS = 30
screen = pygame.display.set_mode((600, 800))
#_________________________________________________________________________
#N = int(input())
N = 1
i = 1
pi = 3.14
#_________________________________________________________________________
# BACK GROUND фон
rect(screen, (128, 102, 0), (0, 400, 800, 800))
rect(screen, (85, 68, 0), (0, 0, 800, 400))
#_________________________________________________________________________
axis_win_x = 0
for win_count in range(3):
    # WINDOWS FRAME рама окна
    rect(screen, (213, 255, 230), (365 - axis_win_x, 60, 210, 260))
    # top glass верхняя часть стекла
    rect(screen, (135, 205, 222), (380 - axis_win_x, 70, 87, 72))
    rect(screen, (135, 205, 222), (475 - axis_win_x, 70, 87, 72))
    # Below Glass нижняя часть стекла
    rect(screen, (135, 205, 222), (380 - axis_win_x, 160, 87, 151))
    rect(screen, (135, 205, 222), (475 - axis_win_x, 160, 87, 151))
    axis_win_x+=250
#_________________________________________________________________________

while i <= N:
    def draw_cat(x, y, k):

        # BODY
        # tail хвост
        ellipse(screen, (200, 113, 55), (x+420//k, y+460//k, 250//k, 80//k))
        ellipse(screen, (78, 45, 21), (x+419//k, y+459//k, 252//k, 82//k), 1)
        # torso торс
        ellipse(screen, (200, 113, 55), (x+50//k, y+420//k, 420//k, 200//k))
        ellipse(screen, (78, 45, 21), (x+49//k, y+419//k, 422//k, 202//k), 1)
        # right paw пр.лапа
        ellipse(screen, (200, 113, 55), (x+36//k, y+500//k, 48//k, 88//k))
        ellipse(screen, (78, 45, 21), (x+35//k, y+499//k, 50//k, 90//k), 1)

        # HEAD голова
        ellipse(screen, (200, 113, 55), (x+15//k, y+430//k, 145//k, 145//k))
        ellipse(screen, (78, 45, 21), (x+14//k, y+429//k, 147//k, 147//k), 1)
        # right ear пр.ухо
        polygon(screen, (200, 113, 55), [(x+10//k, y+430//k), (x+25//k, y+475//k), (x+50//k, y+450//k)])
        polygon(screen, (78, 45, 21), [(x+10//k, y+430//k), (x+25//k, y+475//k), (x+50//k, y+450//k)], 1)
        polygon(screen, (222, 170, 135), [(x+15//k, y+436//k), (x+27//k, y+468//k), (x+44//k, y+450//k)])
        polygon(screen, (78, 45, 21), [(x+15//k, y+436//k), (x+27//k, y+468//k), (x+44//k, y+450//k)], 1)
        # left ear лев.ухо
        polygon(screen, (200, 113, 55), [(x+145//k, y+420//k), (x+110//k, y+446//k), (x+140//k, y+470//k)])
        polygon(screen, (78, 45, 21), [(x+145//k, y+420//k), (x+110//k, y+446//k), (x+140//k, y+470//k)], 1)
        polygon(screen, (222, 170, 135), [(x+141//k, y+427//k), (x+115//k, y+446//k), (x+136//k, y+462//k)])
        polygon(screen, (78, 45, 21), [(x+141//k, y+427//k), (x+115//k, y+446//k), (x+136//k, y+462//k)], 1)
        # right eye пр.глаз
        ellipse(screen, (136, 170, 0), (x+41//k, y+485//k, 35//k, 43//k))
        ellipse(screen, (78, 45, 21), (x+40//k, y+484//k, 37//k, 45//k), 1)
        # right pupil пр.зрачек
        ellipse(screen, (0, 0, 0), (x+60//k, y+488//k, 6//k, 36//k))
        # left eye лев.глаз
        ellipse(screen, (136, 170, 0), (x+101//k, y+485//k, 35//k, 43//k))
        ellipse(screen, (78, 45, 21), (x+100//k, y+484//k, 37//k, 45//k), 1)
        # left pupil лев.зрачек
        ellipse(screen, (0, 0, 0), (x+120//k, y+488//k, 6//k, 36//k))
        # nose
        polygon(screen, (222, 170, 135), [(x+87//k, y+537//k), (x+80//k, y+530//k), (x+94//k, y+530//k)])
        polygon(screen, (78, 45, 21), [(x+87//k, y+537//k), (x+80//k, y+530//k), (x+94//k, y+530//k)], 1)
        # mouth
        pi = 3.14
        polygon(screen, (78, 45, 21), [(x+87//k, y+536//k), (x+87//k, y+548//k), ], 1)
        pygame.draw.arc(screen, (78, 45, 21), (x+82//k, y+494//k, 30//k, 60//k), 4, pi/-3)
        pygame.draw.arc(screen, (78, 45, 21), (x+65//k, y+492//k, 30//k, 60//k), 4, pi/-3)
        # right mustache
        pi = 3.14
        pygame.draw.arc(screen, (78, 45, 21), (x+103//k, y+526//k, 100//k, 80//k), 7, (4*pi)/5)
        pygame.draw.arc(screen, (78, 45, 21), (x+103//k, y+532//k, 100//k, 80//k), 7, (4*pi)/5)
        pygame.draw.arc(screen, (78, 45, 21), (x+103//k, y+538//k, 100//k, 80//k), 7, (4*pi)/5)
        # left mustache
        arc(screen, (78, 45, 21), (x+-27//k, y+526//k, 100//k, 80//k), 7, (4*pi)/5)
        arc(screen, (78, 45, 21), (x+-27//k, y+532//k, 100//k, 80//k), 7, (4*pi)/5)
        arc(screen, (78, 45, 21), (x+-27//k, y+538//k, 100//k, 80//k), 7, (4*pi)/5)

        # PAWS
        ellipse(screen, (200, 113, 55), (x+81//k, y+574//k, 98//k, 53//k))
        ellipse(screen, (78, 45, 21), (x+80//k, y+574//k, 100//k, 55//k), 1)
        # hind paw
        circle(screen, (200, 113, 55), (x+410//k, y+570//k), 65//k)
        circle(screen, (78, 45, 21), (x+410//k, y+570//k), 65//k, 1)
        ellipse(screen, (200, 113, 55), (x+451//k, y+586//k, 37//k, 92//k))
        ellipse(screen, (78, 45, 21), (x+450//k, y+585//k, 39//k, 94//k), 1)


    draw_cat(250, 100 + (150*1), 3)
    i += 1
#_________________________________________________________________________
coil_coord = [[350, 730],
              [100, 640],
              [530, 600],
              [60, 480]]

for coord in coil_coord:
    # clew клубок
    circle(screen, (153, 153, 153), (coord[0], coord[1]), (coord[1]//13))
    circle(screen, (78, 45, 21), (coord[0], coord[1]), (coord[1]//13), 1)
    i = 100
    j = 80
    # lines on the clew
    arc(screen, (78, 45, 21), (coord[0] - 45, coord[1] - 30, i, j), 2, pi)
    arc(screen, (78, 45, 21), (coord[0] - 35, coord[1] - 15, i, j), 2, pi)
    arc(screen, (78, 45, 21), (coord[0] - 25, coord[1] - 0, i, j), 2, pi)
    arc(screen, (78, 45, 21), (coord[0] - 55, coord[1] - 40, i, j), 6, pi/2)
    arc(screen, (78, 45, 21), (coord[0] - 65, coord[1] - 20, i, j), -1/3, pi/5)

#_________________________________________________________________________
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()