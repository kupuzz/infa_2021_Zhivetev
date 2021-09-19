import turtle
import numpy as np
def z(n):
    for i in range(0,n):
        turtle.forward(100)
        turtle.right(180-180/n)
turtle.shape('turtle')
turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.speed(10)
z(5)
turtle.penup()
turtle.goto(150,0)
turtle.pendown()
z(11)
