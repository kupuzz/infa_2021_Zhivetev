import turtle
import numpy as np
turtle.shape('turtle')
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.left(90)
for i in range(0,360):
    turtle.forward(2*np.pi*100/360)
    turtle.left(1)
