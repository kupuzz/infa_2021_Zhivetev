import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(10)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.left(90)
for i in range(0,3600):
    turtle.forward(2*np.pi*(10*i/400)/360)
    turtle.left(1)

