import math
from random import *
import numpy as np

import pygame

f=open('records.txt', 'r')
base=f.read()
f.close()
name=input('Your nickname: ')

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN,BLACK,GREY]

WIDTH = 800
HEIGHT = 600

bullet = 0
balls = []
lemmys = []
s=0

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy-=10/FPS
        if self.x +self.vx> WIDTH-self.r or self.x < self.r:
            self.vx *= -1
        if self.y -self.vy> HEIGHT-self.r or self.y < self.r:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittarget(self, Target):
        if (self.x-Target.x)**2+(self.y-Target.y)**2<=(self.r+Target.r)**2:
            balls.remove(self)
            return True
        else:
            return False
    def hithellraiser(self, Hellraiser):
        if (self.x-(Hellraiser.x+(Hellraiser.r+24)*np.sin(Hellraiser.a)))**2+(self.y-(Hellraiser.y+(Hellraiser.r+24)*np.cos(Hellraiser.a)))**2<24**2:
            balls.remove(self)
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        self.an=math.pi-self.an
        pygame.draw.polygon(self.screen,self.color,[(20+5*math.sin(self.an),450+5*math.cos(self.an)),(20-5*math.sin(self.an),450-5*math.cos(self.an)),
                                                      (20-5*math.sin(self.an)-self.f2_power*math.cos(self.an),450-5*math.cos(self.an)+self.f2_power*math.sin(self.an)),
                                                      (20-5*math.sin(self.an)-self.f2_power*math.cos(self.an)+10*math.sin(self.an),450-5*math.cos(self.an)+self.f2_power*math.sin(self.an)+10*math.cos(self.an))])
        self.an=math.pi-self.an
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self,screen):
        self.points = 0
        self.live = 1
        self.screen=screen
        self.x = randint(600, WIDTH-70)
        self.y = randint(300, HEIGHT-70)
        self.vx = randint(1,10)
        self.vy = randint(1,10)
        self.r = randint(10, 50)
        self.color = RED

    def new_target(self):
        """ Инициализация новой цели. """
        self.points = 0
        self.live = 1
        self.screen=screen
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        self.vx = randint(1,20)
        self.vy = randint(1,20)
        r = self.r = randint(10, 50)
        color = self.color = RED


    def hit(self, points=1):
        """Попадание шарика в цель."""
        global s
        self.points += points
        s+=round(100/self.r)

    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x, self.y),self.r)
        self.x+=self.vx
        self.y+=self.vy
        if self.x> WIDTH-self.r or self.x < self.r:
            self.vx *= -1
        if self.y > HEIGHT-self.r or self.y < self.r:
            self.vy *= -1
class Hellraiser:
    '''
    Создаем класс хеллрейзеров
    '''
    def __init__ (self,screen):
        '''
        Инициализируем переменные:
        x,y - координаты центра, вокруг которого он вращается
        r - радиус вращения
        v - скорость движения
        g -  параметр отображения и попадания
        a - начальный угол поворота
        '''
        self.points = 0
        self.live = 1
        self.x = randint(300, WIDTH-300)
        self.y = randint(250, HEIGHT-250)
        self.r = randint(50,300)
        self.v = randint(10,50)
        self.a = randint(0,100)*2*np.pi

    def new_hellraiser (self):
        '''
        Инициализируем переменные:
        x,y - координаты центра, вокруг которого он вращается
        r - радиус вращения
        v - скорость движения
        g -  параметр отображения и попадания
        a - начальный угол поворота
        '''
        self.points = 0
        self.live = 1
        self.x = randint(300, WIDTH-300)
        self.y = randint(250, HEIGHT-250)
        self.r = randint(50,300)
        self.v = randint(10,50)
        self.a = randint(0,100)*2*np.pi

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global s
        self.points += points
        s+=self.v
        
    def draw(self):
        pygame.draw.polygon(screen,(255,141,11),[(self.x+self.r*np.sin(self.a),self.y+self.r*np.cos(self.a)),
        (self.x+(self.r+35)*np.sin(self.a)-20*np.cos(self.a),self.y+(self.r+35)*np.cos(self.a)+20*np.sin(self.a)),
        (self.x+(self.r+35)*np.sin(self.a)+20*np.cos(self.a),self.y+(self.r+35)*np.cos(self.a)-20*np.sin(self.a))])
        self.a+=self.v/self.r
        if self.x+self.r*np.sin(self.a) >= WIDTH or self.x+self.r*np.sin(self.a) <= 0:
            self.v *= -1
        if self.y+self.r*np.cos(self.a) >= HEIGHT or self.y+self.r*np.cos(self.a) <= 0:
            self.v *= -1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
hellraiser = Hellraiser(screen)

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    hellraiser.draw()
    for b in balls:
        b.draw()
    f2 = pygame.font.Font(None, 80)
    text2 = f2.render('SCORE:', True, RED)
    text3 = f2.render(str(s), True, RED)
    screen.blit(text2,(int(0.35*WIDTH),50))
    screen.blit(text3,(int(0.35*WIDTH)+225,50))
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            F=open('records.txt', 'w')
            F.write(base)
            F.write(str(name)+': '+str(s)+'\n')
            F.close()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittarget(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if b.hithellraiser(hellraiser) and hellraiser.live:
            hellraiser.live = 0
            hellraiser.hit()
            hellraiser.new_hellraiser()
    gun.power_up()

pygame.quit()
