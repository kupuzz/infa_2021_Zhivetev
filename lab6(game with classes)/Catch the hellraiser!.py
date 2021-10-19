import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))
screen.fill((255,255,255))

'''
Считываем все, что есть в файле с рекордами, чтобы презаписать и не потерять
'''
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
balls=[]
lemmys=[]

class Ball:
    '''
    Создаем класс шаров
    '''
    def __init__(self,screen,x,y,dx,dy,r,g,color):
        '''
        Инициализируем переменные шаров:
        x,y - начальные координаты
        dx,dy - скорости по x и y соответственно
        r - радиус шарика
        g -  параметр отображения и попадания
        color - цвет шарика
        '''
        self.screen = screen
        self.x = randint(100, 1100)
        self.y = randint(100, 700)
        self.dx = randint(1,10)
        self.dy = randint(1,10)
        self.r = randint(10, 100)
        self.g = True
        self.color = COLORS[randint(0, 5)]
        
    def draw(self):
        '''
        Рисуем шарик
        '''
        circle(self.screen, self.color, (self.x, self.y), self.r)
        
    def move(self):
        '''
        Двигаем шарик, на месте того, по которому попали, создаем новый, предварительно удалив старый.
        '''
        if self.g:
            self.x+=self.dx
            self.y+=self.dy
        else:
            balls.remove(self)
            x = randint(100, 1100)
            y = randint(100, 700)
            dx = randint(1,10)
            dy = randint(1,10)
            r = randint(10, 100)
            g = True
            color = COLORS[randint(0, 5)]
            balls.append(Ball(screen,x,y,dx,dy,r,g,color))
            
    def hit(self):
        '''
        Обрабатываем попадание по шарику
        '''
        self.g = False
        
    def collision(self):
        '''
        Обрабатываем столкновение шарика со стенами
        '''
        if self.x>=1200-self.r or self.x<=self.r:
            self.dx*=-1
        if self.y>=800-self.r or self.y<=self.r:
            self.dy*=-1
        
class Hellraiser:
    '''
    Создаем класс хеллрейзеров
    '''
    def __init__ (self,screen,x,y,r,v,g,a):
        '''
        Инициализируем переменные:
        x,y - координаты центра, вокруг которого он вращается
        r - радиус вращения
        v - скорость движения
        g -  параметр отображения и попадания
        a - начальный угол поворота
        '''
        self.x = randint(300, 900)
        self.y = randint(300, 500)
        self.r = randint(100,500)
        self.v = randint(10,50)
        self.g = True
        self.a = randint(0,100)*2*np.pi

    def draw(self):
        '''
        Рисуем буйного
        '''
        polygon(screen,(255,141,11),[(self.x+self.r*np.sin(self.a),self.y+self.r*np.cos(self.a)),
        (self.x+(self.r+35)*np.sin(self.a)-20*np.cos(self.a),self.y+(self.r+35)*np.cos(self.a)+20*np.sin(self.a)),
        (self.x+(self.r+35)*np.sin(self.a)+20*np.cos(self.a),self.y+(self.r+35)*np.cos(self.a)-20*np.sin(self.a))])

    def move(self):
        '''
        Двигаем шабутного, удаляем того, по которому попали,создаем вместо него нового 
        '''
        if self.g:
            self.a+=self.v/self.r
        else:
            lemmys.remove(self)
            x = randint(300, 900)
            y = randint(300, 500)
            r = randint(100,500)
            v = randint(10,50)
            g = True
            a = randint(0,100)*2*np.pi
            lemmys.append(Hellraiser(screen,x,y,r,v,g,a))

    def hit(self):
        '''
        Обрабатываем попадание по дикому
        '''
        self.g = False

    def collision(self):
        '''
        Обрабатываем cтолкновение бешеного со стенами
        '''
        if self.x+self.r*np.sin(self.a) >= 1200 or self.x+self.r*np.sin(self.a) <= 0:
            self.v *= -1
        if self.y+self.r*np.cos(self.a) >= 800 or self.y+self.r*np.cos(self.a) <= 0:
            self.v *= -1
    
'''
Создаём пять шариков
'''
for i in range(5):
    x = randint(100, 1100)
    y = randint(100, 700)
    dx = randint(1,10)
    dy = randint(1,10)
    r = randint(10, 100)
    g = True
    color = COLORS[randint(0, 5)]
    balls.append(Ball(screen,x,y,dx,dy,r,g,color))

'''
Создаём двух восставших из ада
'''
for i in range(2):
    x = randint(300, 900)
    y = randint(300, 500)
    r = randint(100,500)
    v = randint(10,50)
    g = True
    a = randint(0,100)*2*np.pi
    lemmys.append(Hellraiser(screen,x,y,r,v,g,a))

    

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            '''
            Записываем при выходе из игры никнейм и счет в файл 
            '''
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
            for ball in balls:
                if (event.pos[0]-ball.x)**2+(event.pos[1]-ball.y)**2<ball.r**2:
                    s+=round(1500/ball.r)
                    ball.hit()
                else:
                    s-=round(ball.r/25)
            '''
            Обрабатываем попадание по буяну, подсчитываем очки
            '''
            for lemmy in lemmys:
                if (event.pos[0]-(lemmy.x+(lemmy.r+24)*np.sin(lemmy.a)))**2+(event.pos[1]-(lemmy.y+(lemmy.r+24)*np.cos(lemmy.a)))**2<24**2:
                    s+=200
                    lemmy.hit()
    '''
    Двигаем,рисуем,отражаем шарики;
    '''
    for ball in balls:
        ball.move()
        ball.draw()
        ball.collision()
    '''
    Двигаем, рисуем, отражаем дебоширов;
    '''
    for lemmy in lemmys:
        lemmy.move()
        lemmy.draw()
        lemmy.collision()

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
