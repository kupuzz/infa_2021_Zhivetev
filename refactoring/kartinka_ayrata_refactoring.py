import pygame
from pygame.draw import *

pygame.init()

FPS = 30
large = 1258
high=500
screen = pygame.display.set_mode((large, high))

def Background(surface,skycolor,groundcolor, x, y, width, height):
    '''
    Функция рисует фон картинки
    surface - объект pygame.Surface
    x,y - координаты верхнего левого угла изображения
    width,height - ширина и высота изображения
    skycolor - цвет неба
    groundcolor - цвет земли
    '''
    sky(surface, skycolor, x, y, width, height/2)
    ground(surface, groundcolor, x, y+height/2, width, high-(y+height/2))

    
def sky(surface, color, x, y, width, height):
    '''
    Функция рисует небо на картинке
    surface - объект pygame.Surface
    x,y - координаты верхнего левого угла неба
    width,height - ширина и высота неба
    color - цвет неба
    '''
    rect(surface, color, (x, y, width, height))

    
def ground(surface, color, x, y, width, height):
    '''
    Функция рисует землю на картинке
    surface - объект pygame.Surface
    x,y - координаты верхнего левого угла земли
    width,height - ширина и высота земли
    color - цвет земли
    '''
    rect(surface, color, (x, y, width, height))


def boy(surface,boy_number,bodycolor,headcolor,armcolor,legcolor,y0,h,r):
    '''
    Функция рисует мальчика
    surface - объект pygame.Surface
    boy_number - номер мальчика слева направо
    bodycolor - цвет тела
    headcolor - цвет головы
    armcolor - цвет рук
    legcolor - цвет ног
    y0 - высота плеч мальчика
    h - высота мальчика
    r - радиус головы
    '''
    a = (-1)**boy_number 
    b = boy_number * large
    boybody(surface,bodycolor, a * 200 + b , y0, a * 100, h)
    head(surface,headcolor, a * 250 + b, y0-30, r)
    boyarms(surface,armcolor,a,b,y0,h)
    boylegs(surface,legcolor,a,b,y0,h)


def boybody(surface,bodycolor,x,y,a,b):
    '''
    Функция рисует тело мальчика
    surface - объект pygame.Surface
    bodycolor - цвет тела
    x,y - координаты верхнего левого края прямоугольника, в который вписан эллипс
    a,b - ширина и высота эллипса
    '''
    ellipse(surface, bodycolor, (x,y,a,b))
def head(surface,headcolor,x,y,r):
    '''
    Функция рисует голову
    surface - объект pygame.Surface
    headcolor - цвет головы
    x,y - координаты центра головы
    r - радиус головы
    '''
    circle(screen, headcolor, (x,y), r)
def boyarms(surface,armcolor,a,b,y0,h):
    '''
    Функция рисует руки мальчика
    surface - объект pygame.Surface
    armcolor - цвет рук
    a,b - параметры положения мальчика
    y0 - высота плеч мальчика
    h - высота мальчика
    '''
    line(surface, armcolor, (a * 220 + b, y0+20), (a * 130 + b, h+60))
    line(surface, armcolor, (a * 280 + b, y0+20), (a * 370 + b, h+60))
def boylegs(surface,legcolor,a,b,y0,h):
    '''
    Функция рисует ноги мальчика
    surface - объект pygame.Surface
    legcolor - цвет ног
    a,b - параметры положения мальчика
    y0 - высота плеч мальчика
    h - высота мальчика
    '''
    lines(surface, legcolor, False, [(a * 220 + b, y0+h-20), (a * 180 + b, y0+h+90), (a * 150 + b, y0+h+95)])
    lines(surface, legcolor, False, [(a * 280 + b, y0+h-25), (a * 300 + b, y0+h+90), (a * 330 + b, y0+h+90)])

  
def girl(surface,girl_number,bodycolor,headcolor,armcolor,legcolor,y0,h,r):
    '''
    Функция рисует девочку
    surface - объект pygame.Surface
    girl_number - номер девочки слева направо
    bodycolor - цвет тела
    headcolor - цвет головы
    armcolor - цвет рук
    legcolor - цвет ног
    y0 - высота плеч девочки
    h - положение нижнего края платья
    r - радиус головы
    '''
    a = (-1)**girl_number 
    b = girl_number * large
    girlbody(surface,bodycolor,a * 500 + b, y0,a * 430 + b, h,a * 570 + b, h)
    head(surface,headcolor,a * 500 + b, 140, 40)
    girlarms(surface,armcolor,a,b,y0)
    girllegs(surface,legcolor,a,b,h)

def girlbody(surface,bodycolor,x1,y1,x2,y2,x3,y3):
    '''
    Функция рисует тело девочки
    surface - объект pygame.Surface
    bodycolor - цвет тела
    x,y - координаты верхнего левого края прямоугольника, в который вписан эллипс
    a,b - ширина и высота эллипса
    '''
    polygon(surface, bodycolor, [(x1,y1), (x2,y2), (x3,y3)])
def girlarms(surface,armcolor,a,b,y0):
    '''
    Функция рисует руки девочки
    surface - объект pygame.Surface
    armcolor - цвет рук
    a,b - параметры положения девочки
    y0 - высота плеч девочки
    '''
    line(surface, armcolor, (a * 490 + b, y0+35), (a * 370 + b, y0+130))
    lines(surface, armcolor, False, [(a * 510 + b, y0+35), (a * 570 + b, y0+65), (a * 630 + b, y0+40)])
def girllegs(surface,legcolor,a,b,h):
    '''
    Функция рисует ноги девочки
    surface - объект pygame.Surface
    armcolor - цвет ног
    a,b - параметры положения девочки
        h - положение нижнего края платья
    '''
    lines(surface, legcolor, False, [(a * 480 + b, h), (a * 480 + b, h+80), (a * 450 + b, h+85)])
    lines(surface, legcolor, False, [(a * 520 + b, h), (a * 520 + b, h+80), (a * 550 + b, h+80)])
    
    
def Balloon(surface,threadcolor,ballooncolor,x1,y1):
    '''
    Функция рисует воздушный шарик на нити
    surface - объект pygame.Surface
    threadcolor - цвет нити
    ballooncolor - цвет шарика
    x1,y1 - положение конца руки держащего шарик
    '''
    thread(surface,threadcolor,x1,y1,x1-40,y1-105)
    balloon(surface,ballooncolor,x1,y1)
def thread(surface,threadcolor,x1,y1,x2,y2):
    '''
    Функция рисует нить для воздушного шарика
    surface - объект pygame.Surface
    threadcolor - цвет нити
    x1,y1 - координаты первого конца нити
    x2,y2 - координаты второго конца нити
    '''
    line(surface, threadcolor, (x1,y1), (x2,y2))
def balloon(surface,ballooncolor,x1,y1):
    '''
    Функция рисует воздушный шарик
    surface - объект pygame.Surface
    ballooncolor - цвет шарика
    x1,y1 - положение конца руки держащего шарик
    '''
    polygon(surface, ballooncolor, [(x1-40, y1-105), (x1-50, y1-175), (x1-95, y1-140)])
    circle(surface, ballooncolor, (x1-70, y1-180), 20)
    circle(surface, ballooncolor, (x1-90, y1-160), 20)


def IceCream1(surface,armcolor,cupcolor,color1,color2,color3,x1,y1):
    '''
    Функция рисует мороженое в руке
    surface - объект pygame.Surface
    cupcolor - цвет стаканчика
    armcolor - цвет руки
    color1 - цвет 1 шарика мороженого
    color2 - цвет 2 шарика мороженого
    color3 - цвет 3 шарика мороженого
    x1,y1 - положение конца руки держащего мороженое
    '''
    piece_of_arm(surface,armcolor,x1,y1)
    cup1(surface,cupcolor,x1,y1)
    scoops1(surface,color1,color2,color3,x1,y1)

def piece_of_arm(surface,armcolor,x1,y1):
    '''
    Функция рисует кусок руки))))
    surface - объект pygame.Surface
    armcolor - цвет руки
    x1,y1 - положение конца руки держащего мороженое
    '''
    line(surface, armcolor, (x1,y1), (x1+10, y1-80))
def cup1(surface,cupcolor,x1,y1):
    '''
    Функция рисует стаканчик от мороженого
    surface - объект pygame.Surface
    cupcolor - цвет стаканчика
    x1,y1 - положение конца руки держащего мороженое
    '''
    polygon(surface, cupcolor, [(x1+10, y1-80), (x1+30, y1-140), (x1-10, y1-140)])
def scoops1(surface,color1,color2,color3,x1,y1):
    '''
    Функция рисует шарики мороженого
    surface - объект pygame.Surface
    color1 - цвет 1 шарика мороженого
    color2 - цвет 2 шарика мороженого
    color3 - цвет 3 шарика мороженого
    x1,y1 - положение конца руки держащего мороженое
    '''
    circle(surface, color1, (x1+20, y1-155), 20)
    circle(surface, color2, (x1, y1-155), 20)
    circle(surface, color3, (x1+10, y1-170), 20)


def IceCream2(surface,cupcolor,color1,color2,color3,x1,y1):
    '''
    Функция рисует мороженое
    surface - объект pygame.Surface
    cupcolor - цвет стаканчика
    color1 - цвет 1 шарика мороженого
    color2 - цвет 2 шарика мороженого
    color3 - цвет 3 шарика мороженого
    x1,y1 - положение конца руки держащего мороженое
    '''
    cup2(surface,cupcolor,x1,y1)
    scoops2(surface,color1,color2,color3,x1,y1)

def cup2(surface,cupcolor,x1,y1):
    '''
    Функция рисует стаканчик от мороженого
    surface - объект pygame.Surface
    cupcolor - цвет стаканчика
    x1,y1 - положение конца руки держащего мороженое
    '''
    polygon(surface, cupcolor, [(x1, y1), (x1+10, y1-70), (x1+50, y1-35)])
def scoops2(surface,color1,color2,color3,x1,y1):
    '''
    Функция рисует шарики мороженого
    surface - объект pygame.Surface
    color1 - цвет 1 шарика мороженого
    color2 - цвет 2 шарика мороженого
    color3 - цвет 3 шарика мороженого
    x1,y1 - положение конца руки держащего мороженое
    '''
    circle(surface, color1, (x1+30, y1-75), 20)
    circle(surface, color2, (x1+50, y1-55), 20)
    circle(surface, color3, (x1+50, y1-85), 20)


Background(screen,(135, 206, 235),(60, 179, 113), 0,0,large,high)

for boy_number in range(2):
    boy(screen,boy_number,(119, 136, 153),(255, 228, 196),(0, 0, 0),(0, 0, 0),150,220,40)

for girl_number in range(2):
    girl(screen,girl_number,(255, 20, 147),(255, 228, 196),(0, 0, 0),(0, 0, 0),150,370,40)

Balloon(screen,(0, 0, 0),(255, 0, 0),140,280)

IceCream1(screen,(0, 0, 0),(255, 165, 0),(255, 0, 0),(160, 82, 45),(255, 245, 238),630,190)

IceCream2(screen,(255, 165, 0),(255, 0, 0),(160, 82, 45),(255, 245, 238),1120,290)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
