import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (217, 233, 235), (0,0,400,400))
circle(screen, (213, 233, 0), (200, 200), 100)
rect(screen, (0, 0, 0), (150, 250, 100, 22))
circle(screen, (255, 0, 0), (250, 170), 17)
circle(screen, (255, 0, 0), (150, 170), 25)
circle(screen, (0, 0, 0), (250, 170), 7)
circle(screen, (0, 0, 0), (150, 170), 10)
polygon(screen, (0, 0, 0), [(220,160), (226,168),(296,128),(290,120) ])
polygon(screen, (0, 0, 0), [(100,118), (104,110),(186,160),(180,168) ])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
