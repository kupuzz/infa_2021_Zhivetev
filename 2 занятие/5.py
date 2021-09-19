import turtle
import numpy as np
turtle.shape('turtle')
for i in range(0,10):
    turtle.forward(10+20*i)
    turtle.left(90)
    turtle.forward(10+20*i)
    turtle.left(90)
    turtle.forward(10+20*i)
    turtle.left(90)
    turtle.forward(10+20*i)
    turtle.penup()
    turtle.forward(10)

    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()
