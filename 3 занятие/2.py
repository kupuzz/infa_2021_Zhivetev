import turtle
import numpy as np
from random import *
turtle.speed(10)
turtle.shape('turtle')
turtle.color('blue')
a0=[(30,90,1),(60,90,1),(30,90,1),(60,90,1),(40,0,0)]
a1=[(30,135,0),(42,180,1),(42,135,0),(60,180,1),(60,90,0),(10,0,0)]
a2=[(30,90,1),(30,45,1),(42,225,1),(30,270,1),(60,90,0),(10,0,0)]
a3=[(30,135,1),(42,225,1),(30,135,1),(42,225,1),(30,270,0),(60,90,0),(10,0,0)]
a4=[(0,90,0),(30,270,1),(30,270,1),(30,180,1),(60,180,1),(60,90,0),(10,0,0)]
a5=[(30,180,1),(30,270,0),(30,270,1),(30,90,1),(30,90,1),(30,180,1),(30,270,0),(60,90,0),(10,0,0)]
a6=[(30,135,0),(42,225,1),(30,90,1),(30,90,1),(30,90,1),(30,90,1),(30,270,0),(30,90,0),(10,0,0)]
a7=[(30,135,1),(42,315,1),(30,180,1),(60,90,0),(40,0,0)]
a8=[(30,90,1),(60,90,1),(30,90,1),(60,180,1),(30,270,0),(30,270,1),(30,90,0),(10,0,0)]
a9=[(30,90,1),(30,90,1),(30,90,1),(30,90,1),(30,90,0),(30,45,0),(42,180,1),(42,315,0),(30,90,0),(10,0,0)]
print(a1)
for i in a1:
    if i[2]==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(i[0])
    turtle.right(i[1])
for i in a4:
    if i[2]==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(i[0])
    turtle.right(i[1])
for i in a1:
    if i[2]==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(i[0])
    turtle.right(i[1])
for i in a7:
    if i[2]==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(i[0])
    turtle.right(i[1])
for i in a0:
    if i[2]==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(i[0])
    turtle.right(i[1])
for i in a0:
    if i[2]==0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(i[0])
    turtle.right(i[1])
        

