import pygame
from pygame.draw import *
def f(x,b,h,e,s,n,m,z):
    circle(screen, b, (x, 480), 150)
    circle(screen, s, (x, 250), 130)
    polygon(screen, m, [(x-70,275), (x+70,275),(x,320)])
    polygon(screen, n, [(x-10,247), (x+10,247),(x,265)])
    polygon(screen, (0,0,0), [(x-70,275), (x+70,275),(x,320)],1)
    polygon(screen, (0,0,0), [(x-10,247), (x+10,247),(x,265)],1)
    circle(screen, e, (x+50, 210), 25)
    circle(screen, e, (x-50, 210), 25)
    circle(screen, (0,0,0), (x+50, 210), 25,1)
    circle(screen, (0,0,0), (x-50, 210), 25,1)
    circle(screen, z, (x+50, 215), 7)
    circle(screen, z, (x-50, 215), 7)
    polygon(screen, s, [(x+115,360), (x+127,369),(x+230,40),
                                            (x+218,31)])
    polygon(screen, s, [(x-115,360), (x-127,369),(x-230,40),
                                            (x-218,31)])
    circle(screen, s, (x+215,40), 25)
    circle(screen, s, (x-215,40), 25)
    polygon(screen, b, [(x+80,360), (x+110,320),(x+150,335),
                                            (x+150,385),(x+110,400)])
    polygon(screen, b, [(x-80,360), (x-110,320),(x-150,335),
                                            (x-150,385),(x-110,400)])
    polygon(screen, (0,0,0), [(x+80,360), (x+110,320),(x+150,335),
                                            (x+150,385),(x+110,400)],1)
    polygon(screen, (0,0,0), [(x-80,360), (x-110,320),(x-150,335),
                                            (x-150,385),(x-110,400)],1)
    polygon(screen, h, [(x-92,158),(x-71,137),(x-92,128)])
    polygon(screen, (0,0,0), [(x-92,158),(x-71,137),(x-92,128)],1)
    polygon(screen, h, [(x-75,144),(x-50,127),(x-75,114)])
    polygon(screen, (0,0,0), [(x-75,144),(x-50,127),(x-75,114)],1)
    polygon(screen, h, [(x-55,132),(x-28,119),(x-55,102)])
    polygon(screen, (0,0,0), [(x-55,132),(x-28,119),(x-55,102)],1)
    polygon(screen, h, [(x-34,124),(x-5,116),(x-30,94)])
    polygon(screen, (0,0,0), [(x-34,124),(x-5,116),(x-30,94)],1)
    polygon(screen, h, [(x-11,120),(x+19,117),(x,90)])
    polygon(screen, (0,0,0), [(x-11,120),(x+19,117),(x,90)],1)
    polygon(screen, h, [(x+11,121),(x+41,124),(x+24,98)])
    polygon(screen, (0,0,0), [(x+11,121),(x+41,124),(x+24,98)],1)
    polygon(screen, h, [(x+34,124),(x+63,132),(x+52,100)])
    polygon(screen, (0,0,0), [(x+34,124),(x+63,132),(x+52,100)],1)
    polygon(screen, h, [(x+55,132),(x+82,145),(x+70,112)])
    polygon(screen, (0,0,0), [(x+55,132),(x+82,145),(x+70,112)],1)
    polygon(screen, h, [(x+75,144),(x+100,161),(x+94,128)])
    polygon(screen, (0,0,0), [(x+75,144),(x+100,161),(x+94,128)],1)
    polygon(screen, h, [(x+92,158),(x+108,179),(x+108,148)])
    polygon(screen, (0,0,0), [(x+92,158),(x+108,179),(x+108,148)],1)
    
x=300#координата центра головы
b=(255, 117, 34)#цвет тела 
h=(180, 0, 227)#цвет волос
e=(1, 215, 232)#цвет глаз
s=(255, 220, 185)#цвет кожи
n=(87, 0, 2)#цвет носа
m=(255, 0, 0)#цвет рта
z=(0, 0, 0)#цвет зрачков

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1010, 450))
screen.fill((255,255,255))

f(290,(1, 100, 1),(226, 226, 0),(205, 230, 212),s,n,m,z)
f(720,b,h,e,s,n,m,z)

rect(screen, (0, 254, 0), (40, 0, 930, 45))
rect(screen, (0, 0, 0), (40, 0, 930, 45),1)
f1 = pygame.font.Font(None, 80)
text1 = f1.render('PYTHON is REALLY AMAZING!', True,
                  (0, 0, 0))
screen.blit(text1,(80,0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
