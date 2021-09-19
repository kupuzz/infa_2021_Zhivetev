import turtle
import numpy as np
def mn(n):
    turtle.left(180)
    turtle.right((180-(360/n))/2)
    for i in range(0,n):

        turtle.forward(10*n*2*np.sin(2*np.pi/n))
        turtle.left(360/n)
    turtle.left((180-(360/n))/2)
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
turtle.shape('turtle')
turtle.speed(10)
for i in range(3,13):
    mn(i)


