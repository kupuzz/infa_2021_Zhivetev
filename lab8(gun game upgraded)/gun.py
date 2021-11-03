import math
from random import *
import numpy as np

import pygame

print('''Ознакомтесь с управлением:
      a - перемещение зеленого танка влево,
      d - перемещение зеленого танка вправо,
      w - подъем пушки зеленого танка вверх,
      s - опускание пушки зеленого такнка вниз,
      q - стрельба из пушки зеленого танка,
      LEFT - перемещение серого танка влево,
      RIGHT - перемещение серого танка вправо,
      UP - подъем пушки серого танка вверх,
      DOWN - опускание пушки серого танка вниз,
      Numpad 0 - стрельба из пушки серого танка,

      ''')

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
rocket = 0
balls = []
rockets = []
lemmys = []
bombs=[]
bomb=0
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
        global bullet
        if (self.x-Target.x)**2+(self.y-Target.y)**2<=(self.r+Target.r)**2:
            balls.remove(self)
            bullet-=1
            return True
        else:
            return False
    def hithellraiser(self, Hellraiser):
        global bullet
        if (self.x-(Hellraiser.x+(Hellraiser.r+24)*np.sin(Hellraiser.a)))**2+(self.y-(Hellraiser.y+(Hellraiser.r+24)*np.cos(Hellraiser.a)))**2<24**2:
            balls.remove(self)
            bullet-=1
            return True
        else:
            return False
    def hitgun2(self, Gun2):
        global bullet
        if (self.x-Gun2.x)**2+(self.y-Gun2.y)**2<=(5)**2:
            balls.remove(self)
            bullet-=1
            Gun2.x=-300
            Gun2.y=-300
            return True
        else:
            return False

class Rocket:
    def __init__(self, screen: pygame.Surface, x=780, y=450):
        """ Конструктор класса Rocket

        Args:
        x - начальное положение ракеты по горизонтали
        y - начальное положение ракеты по вертикали
        """
        self.screen = screen
        self.an = 0
        self.x = x
        self.y = y
        self.l = 5
        self.h = 20
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить ракеты по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if self.x > WIDTH or self.x < 0:
            self.vx *= -1
            self.an=np.pi-self.an
        if self.y > HEIGHT or self.y < 0:
            self.vy *= -1
            self.an=np.pi-self.an

    def draw(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x+self.l/2*math.sin(self.an),self.y+self.l/2*math.cos(self.an)),(self.x-self.l/2*math.sin(self.an),self.y-self.l/2*math.cos(self.an)),
                            (self.x-self.l/2*math.sin(self.an)-self.h*math.cos(self.an),self.y-self.l/2*math.cos(self.an)+self.h*math.sin(self.an)),
                            (self.x-self.l/2*math.sin(self.an)-self.h*math.cos(self.an)+self.l*math.sin(self.an),self.y-self.l/2*math.cos(self.an)+self.h*math.sin(self.an)+self.l*math.cos(self.an))])

    def hittarget(self, Target):
        global rocket
        if (self.x-Target.x)**2+(self.y-Target.y)**2<=(Target.r)**2:
            rockets.remove(self)
            rocket-=1
            return True
        else:
            return False
    def hithellraiser(self, Hellraiser):
        global rocket
        if (self.x-(Hellraiser.x+(Hellraiser.r+24)*np.sin(Hellraiser.a)))**2+(self.y-(Hellraiser.y+(Hellraiser.r+24)*np.cos(Hellraiser.a)))**2<24**2:
            rockets.remove(self)
            rocket-=1
            return True
        else:
            return False
    def hitgun1(self, Gun1):
        global rocket
        if (self.x-Gun1.x)**2+(self.y-Gun1.y)**2<=(5)**2:
            rockets.remove(self)
            rocket-=1
            Gun1.x=-300
            Gun1.y=-300
            return True
        else:
            return False

class Bombs:
    
    def __init__(self,screen: pygame.Surface):
        self.screen = screen
        self.x=800
        self.y=600
        self.v=5
        self.color = RED

    def move(self):
        global bomb
        if self.y>600:
            bombs.remove(self)
            bomb-=1
        self.y+=self.v

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, [(self.x-5,self.y),(self.x+5,self.y),(self.x+5,self.y+10),(self.x,self.y+30),(self.x-5,self.y+10)])
        
    def hitgun1(self, Gun1):
        global bomb
        if (self.x-Gun1.x)**2+(self.y-Gun1.y)**2<=(3)**2:
            bombs.remove(self)
            bomb-=1
            Gun1.x=-300
            Gun1.y=-300
            return True
        else:
            return False

class Gun1:
    def __init__(self, screen,x,y):
        self.screen = screen
        self.f1_power = 50
        self.f1_on = 0
        self.an = -1
        self.color = GREEN
        self.x = x
        self.y = y

    def fire1_start(self, event):
        self.f1_on = 1

    def fire1_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки q.
        """
        global bullet
        if bullet<=4:
            bullet += 1
            new_ball = Ball(self.screen)
            new_ball.r += 5
            new_ball.x=self.x+self.f1_power*math.cos(self.an)
            new_ball.y=self.y+self.f1_power*math.sin(self.an)
            new_ball.vx = self.f1_power * math.cos(self.an)/5
            new_ball.vy = - self.f1_power * math.sin(self.an)/5
            balls.append(new_ball)
            self.f1_on = 0
            self.f1_power = 50

    def targetting1up(self, event):
        self.an += np.pi/45
        
    def targetting1down(self, event):
        self.an -= np.pi/45

    def draw(self):
        self.an=math.pi-self.an
        pygame.draw.polygon(self.screen,self.color,[(self.x-30,self.y),(self.x+30,self.y),(self.x+44,self.y+24),(self.x-40,self.y+24)])
        pygame.draw.circle(self.screen,self.color,(self.x,self.y+5),15)
        pygame.draw.polygon(self.screen,self.color,[(self.x+5*math.sin(self.an),self.y+5*math.cos(self.an)),(self.x-5*math.sin(self.an),self.y-5*math.cos(self.an)),
                                                      (self.x-5*math.sin(self.an)-self.f1_power*math.cos(self.an),self.y-5*math.cos(self.an)+self.f1_power*math.sin(self.an)),
                                                      (self.x-5*math.sin(self.an)-self.f1_power*math.cos(self.an)+10*math.sin(self.an),self.y-5*math.cos(self.an)+self.f1_power*math.sin(self.an)+10*math.cos(self.an))])
        self.an=math.pi-self.an
        
    def moveright(self):
        self.x+=10
        
    def moveleft(self):
        self.x-=10
        
    def power_up(self):
        if self.f1_on and bullet<=4:
            if self.f1_power < 100:
                self.f1_power += 1

class Gun2:
    def __init__(self, screen,x,y):
        self.screen = screen
        self.f2_power = 50
        self.f2_on = 0
        self.an = np.pi
        self.color = GREY
        self.x = x
        self.y = y
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел ракетой.

        Происходит при отпускании кнопки 0.
        """
        global rocket
        if rocket<=4:
            rocket += 1
            new_rocket = Rocket(self.screen)
            new_rocket.an = np.pi-self.an
            new_rocket.x=self.x+self.f2_power*math.cos(self.an)
            new_rocket.y=self.y+self.f2_power*math.sin(self.an)
            new_rocket.vx = self.f2_power * math.cos(self.an)
            new_rocket.vy = - self.f2_power * math.sin(self.an)
            rockets.append(new_rocket)
            self.f2_on = 0
            self.f2_power = 50

    def targetting2up(self, event):
        self.an += np.pi/45
        
    def targetting2down(self, event):
        self.an -= np.pi/45

    def draw(self):
        self.an=math.pi-self.an
        pygame.draw.polygon(self.screen,self.color,[(self.x-35,self.y),(self.x+35,self.y),(self.x+35,self.y+30),(self.x-40,self.y+30)])
        pygame.draw.polygon(self.screen,self.color,[(self.x-10,self.y),(self.x+10,self.y),(self.x+10,self.y-10),(self.x-10,self.y-10)])
        pygame.draw.polygon(self.screen,self.color,[(self.x+5*math.sin(self.an),self.y+5*math.cos(self.an)),(self.x-5*math.sin(self.an),self.y-5*math.cos(self.an)),
                                                      (self.x-5*math.sin(self.an)-self.f2_power*math.cos(self.an),self.y-5*math.cos(self.an)+self.f2_power*math.sin(self.an)),
                                                      (self.x-5*math.sin(self.an)-self.f2_power*math.cos(self.an)+10*math.sin(self.an),self.y-5*math.cos(self.an)+self.f2_power*math.sin(self.an)+10*math.cos(self.an))])
        self.an=math.pi-self.an
        
    def moveright(self):
        self.x+=10
        
    def moveleft(self):
        self.x-=10
        
    def power_up(self):
        if self.f2_on and rocket<=4:
            if self.f2_power < 100:
                self.f2_power += 1

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

    def spawnbomb(self,Gun):
        if np.abs(self.x-Gun.x)<=2 and -self.y+Gun.y>200:
            global bomb
            bomb+=1
            new_bomb=Bombs(screen)
            new_bomb.x=self.x
            new_bomb.y=self.y
            bombs.append(new_bomb)

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
        self.r = randint(50,200)
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
        self.r = randint(50,200)
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

    def spawnbomb(self,Gun):
        if np.abs(self.x+self.r*np.sin(self.a)-Gun.x)<=2 and -self.y-self.r*np.cos(self.a)+Gun.y<200:
            global bomb
            bomb+=1
            new_bomb=Bombs(screen)
            new_bomb.color = (255,141,11)
            new_bomb.x=self.x+self.r*np.sin(self.a)
            new_bomb.y=self.y
            bombs.append(new_bomb)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()
gun1 = Gun1(screen,60,500)
gun2 = Gun2(screen,740,500)
target = Target(screen)
hellraiser = Hellraiser(screen)

finished = False

while not finished:
    screen.fill(WHITE)
    gun1.draw()
    gun2.draw()
    target.draw()
    hellraiser.draw()
    for b in balls:
        b.draw()
    for r in rockets:
        r.draw()
    for b in bombs:
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            gun1.fire1_start(event)
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            gun1.fire1_end(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            gun1.targetting1down(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            gun1.targetting1up(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            gun1.moveleft()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            gun1.moveright()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
            gun2.fire2_start(event)
        if event.type == pygame.KEYUP and event.key == pygame.K_KP0:
            gun2.fire2_end(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            gun2.targetting2up(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            gun2.targetting2down(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            gun2.moveleft()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            gun2.moveright()
    target.spawnbomb(gun1)
    target.spawnbomb(gun2)
    hellraiser.spawnbomb(gun1)
    hellraiser.spawnbomb(gun2)
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
        b.hitgun2(gun2)

    for r in rockets:
        r.move()
        if r.hittarget(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if r.hithellraiser(hellraiser) and hellraiser.live:
            hellraiser.live = 0
            hellraiser.hit()
            hellraiser.new_hellraiser()
        r.hitgun1(gun1)

    for b in bombs:
        b.move()
        b.hitgun1(gun1)
        b.hitgun1(gun2)
        
    gun1.power_up()
    gun2.power_up()

pygame.quit()
