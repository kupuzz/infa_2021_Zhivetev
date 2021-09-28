import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 450))
screen.fill((255,255,255))

circle(screen, (255, 117, 34), (300, 480), 150)
circle(screen, (255, 220, 185), (300, 250), 130)
polygon(screen, (255, 0, 0), [(230,275), (370,275),(300,320)])
polygon(screen, (0, 0, 0), [(230,275), (370,275),(300,320)],1)
polygon(screen, (87, 0, 2), [(290,247), (310,247),(300,265)])
polygon(screen, (0, 0, 0), [(290,247), (310,247),(300,265)],1)
circle(screen, (1, 215, 232), (350, 210), 25)
circle(screen, (0,0,0), (350, 210), 25,1)
circle(screen, (1, 215, 232), (250, 210), 25)
circle(screen, (0,0,0), (250, 210), 25,1)
circle(screen, (0, 0, 0), (350, 215), 7)
circle(screen, (0, 0, 0), (250, 215), 7)
polygon(screen, (255, 220, 185), [(415,360), (427,369),(530,40),
                                            (518,31)])
polygon(screen, (255, 220, 185), [(185,360), (173,369),(70,40),
                                            (82,31)])
circle(screen, (255, 220, 185), (515,40), 25)
circle(screen, (255, 220, 185), (85,40), 25)
rect(screen, (0, 254, 0), (40, 0, 520, 45))
rect(screen, (0, 0, 0), (40, 0, 520, 45),1)
polygon(screen, (255, 117, 34), [(380,360), (410,320),(450,335),
                                            (450,385),(410,400)])
polygon(screen, (0,0,0), [(380,360), (410,320),(450,335),
                                            (450,385),(410,400)],1)
polygon(screen, (255, 117, 34), [(220,360), (190,320),(150,335),
                                            (150,385),(190,400)])
polygon(screen, (0,0,0), [(220,360), (190,320),(150,335),
                                            (150,385),(190,400)],1)
f1 = pygame.font.Font(None, 72)
text1 = f1.render('PYTHON is AMAZING', True,
                  (0, 0, 0))
screen.blit(text1,(38,0))
polygon(screen, (180, 0, 227), [(208,158),(229,137),(208,128)])
polygon(screen, (0, 0, 0), [(208,158),(229,137),(208,128)],1)
polygon(screen, (180, 0, 227), [(225,144),(250,127),(225,114)])
polygon(screen, (0, 0, 0), [(225,144),(250,127),(225,114)],1)
polygon(screen, (180, 0, 227), [(245,132),(272,119),(245,102)])
polygon(screen, (0,0,0), [(245,132),(272,119),(245,102)],1)
polygon(screen, (180, 0, 227), [(266,124),(295,116),(270,94)])
polygon(screen, (0,0,0), [(266,124),(295,116),(270,94)],1)
polygon(screen, (180, 0, 227), [(289,120),(319,117),(300,90)])
polygon(screen, (0,0,0), [(289,120),(319,117),(300,90)],1)
polygon(screen, (180, 0, 227), [(311,121),(341,124),(324,98)])
polygon(screen, (0,0,0), [(311,121),(341,124),(324,98)],1)
polygon(screen, (180, 0, 227), [(334,124),(363,132),(352,100)])
polygon(screen, (0,0,0), [(334,124),(363,132),(352,100)],1)
polygon(screen, (180, 0, 227), [(355,132),(382,145),(370,112)])
polygon(screen, (0,0,0), [(355,132),(382,145),(370,112)],1)
polygon(screen, (180, 0, 227), [(375,144),(400,161),(394,128)])
polygon(screen, (0,0,0), [(375,144),(400,161),(394,128)],1)
polygon(screen, (180, 0, 227), [(392,158),(408,179),(408,148)])
polygon(screen, (0,0,0), [(392,158),(408,179),(408,148)],1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
