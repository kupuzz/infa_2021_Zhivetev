from random import *
import turtle


number_of_turtles = 40
steps_of_time_number = 1000
turtle.speed(100)
turtle.hideturtle()
turtle.penup()
turtle.goto(-220,-220)
turtle.pendown()
for i in range(4):
    turtle.forward(440)
    turtle.left(90)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]


for unit in pool:
    unit.penup()
    unit.speed(100)
    unit.right(360*random())
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(10)
        if unit.xcor()<-200:
            unit.right(180)
        if unit.xcor()>200:
            unit.right(180)
        if unit.ycor()<-200:
            unit.right(180)
        if unit.ycor()>200:
            unit.right(180)
        
        
