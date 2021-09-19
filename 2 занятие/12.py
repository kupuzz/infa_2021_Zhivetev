import turtle
import numpy as np
def d(r):
    for i in range(0,180):
        turtle.forward(2*np.pi*(r)/360)
        turtle.right(1)
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
for i in range(1,8):
    d(50)
    d(10)


