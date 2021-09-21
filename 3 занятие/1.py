import turtle
import numpy as np
from random import *
turtle.speed(10)
turtle.shape('turtle')
for i in range(10000):
    turtle.forward(50*random())
    turtle.left(360*random())
