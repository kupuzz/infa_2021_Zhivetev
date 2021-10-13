import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))
screen.fill((255,255,255))

f=open('records.txt', 'r')
base=f.read()
f.close()
name=input('Your nickname: ')

'''
Создаем все нужные цвета, массивы, переменные
'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
s=0
balls=[[]*7]*5
ball=[]
ozzy=[[]*6]*2
lemmy=[]

def new_ball():
    '''
    Создаёт новый шарик
    x,y - начальные координаты
    dx,dy - скорости по x и y соответственно
    r - радиус шарика
    g -  параметр отображения и попадания
    color - цвет шарика
    '''
    x = randint(100, 1100)
    dx = randint(1,10)
    y = randint(100, 700)
    dy = randint(1,10)
    r = randint(10, 100)
    g=0
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    ball=[x,y,dx,dy,color,r,g]
    return(ball)

def hellraiser():
    '''
    Создает хеллрейзера
    x,y - координаты центра, вокруг которого он вращается
    r - радиус вращения
    v - скорость движения
    g -  параметр отображения и попадания
    a - начальный угол поворота
    '''
    x = randint(300, 900)
    y = randint(300, 500)
    r = randint(100,500)
    v = randint(10,50)
    g = 0
    a = randint(0,100)*2*np.pi
    if x+(r+40)*np.sin(a)>1200 or x+(r+40)*np.sin(a)<0 or y+(r+40)*np.cos(a)>800 or y+(r+40)*np.cos(a)<0:
        hellraiser()
    lemmy=[x,y,r,v,g,a]
    return(lemmy)
    
'''
Создаём пять шариков
'''
for i in range(5):
    new_ball()
    balls[i]=new_ball()

'''
Создаём двух восставших из ада
'''
for i in range(2):
    hellraiser()
    ozzy[i]=hellraiser()
    

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            F=open('records.txt', 'w')
            F.write(base)
            F.write(str(name)+': '+str(s)+'\n')
            F.close()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''
            Создаем надпись Click! в месте нажатия мышкой
            '''
            f1 = pygame.font.Font(None, 50)
            text1 = f1.render('Click!', True,RED)
            screen.blit(text1,(event.pos[0]-45,event.pos[1]))
            '''
            Обрабатываем попадание по шарику, подсчитываем очки
            '''
            for i in range (5):
                if (event.pos[0]-balls[i][0])**2+(event.pos[1]-balls[i][1])**2<balls[i][5]**2:
                    s+=round(1500/balls[i][5])
                    balls[i][6]=1
                else:
                    s-=round(balls[i][5]/25)
            '''
            Обрабатываем попадание по буяну, подсчитываем очки
            '''
            for i in range (2):
                if (event.pos[0]-(ozzy[i][0]+(ozzy[i][2]+24)*np.sin(ozzy[i][5])))**2+(event.pos[1]-(ozzy[i][1]+(ozzy[i][2]+24)*np.cos(ozzy[i][5])))**2<24**2:
                    s+=200
                    ozzy[i][4]=1
    '''
    Двигаем шарики; вместо того, по которому попали, создаем новый
    '''
    for i in range(5):
        if balls[i][6]==0:
            balls[i][0] += balls[i][2]
            balls[i][1] += balls[i][3]
            circle(screen, balls[i][4], (balls[i][0], balls[i][1]), balls[i][5])
            if balls[i][0] >= 1200-balls[i][5] or balls[i][0] <= balls[i][5]:
                balls[i][2] *= -1
            if balls[i][1] >= 800-balls[i][5] or balls[i][1] <= balls[i][5]:
                balls[i][3] *= -1
        if balls[i][6]==1:
            new_ball()
            ball=new_ball()
            balls[i]=ball
    '''
    Двигаем дебоширов; вместо того, по которому попали, создаём нового
    '''
    for i in range(2):
        if ozzy[i][4]==0:
            ozzy[i][5]+=ozzy[i][3]/ozzy[i][2]
            a = ozzy[i][5]
            x = ozzy[i][0]
            y = ozzy[i][1]
            r = ozzy[i][2]
            polygon(screen,(255,141,11),[(x+r*np.sin(a),y+r*np.cos(a)),
                                         (x+(r+35)*np.sin(a)-20*np.cos(a),y+(r+35)*np.cos(a)+20*np.sin(a)),
                                         (x+(r+35)*np.sin(a)+20*np.cos(a),y+(r+35)*np.cos(a)-20*np.sin(a))])
            if x+r*np.sin(a) >= 1200 or x+r*np.sin(a) <= 0:
                ozzy[i][3] *= -1
            if y+r*np.cos(a) >= 800 or y+r*np.cos(a) <= 0:
                ozzy[i][3] *= -1
        if ozzy[i][4]==1:
            hellraiser()
            ozzy[i]=hellraiser()
    '''
    Выводим счёт на экран
    '''
    f2 = pygame.font.Font(None, 80)
    text2 = f2.render('SCORE:', True, RED)
    text3 = f2.render(str(s), True, RED)
    screen.blit(text2,(425,50))
    screen.blit(text3,(650,50))
    pygame.display.update()
    screen.fill((255,255,255))

pygame.quit()
