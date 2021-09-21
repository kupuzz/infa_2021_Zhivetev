import turtle
import numpy as np
from random import *
turtle.speed(10)
turtle.shape('circle')
turtle.speed(100)
turtle.goto(1000,0)
turtle.goto(0,0)
turtle.speed(10)
Vx=30
Vy=50
ay=-10
x=0
y=0
k=-0.1
dt=0.1
for i in range(1000):
    turtle.goto(x,y)
    x+=Vx*dt
    y+=Vy*dt
    Vx+=k*Vx*dt
    Vy+=ay*dt+k*Vy*dt
    if y<0:
        Vy=-Vy

