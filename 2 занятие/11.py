import turtle
import numpy as np
def s(n):
    for i in range(0,36):
        turtle.forward(2*np.pi*(100*n+500)/360)
        turtle.left(10)
    for i in range(0,36):
        turtle.forward(2*np.pi*(100*n+500)/360)
        turtle.right(10)
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
for i in range(1,8):
    s(i)


