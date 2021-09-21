import turtle
import numpy as np
from random import *
a0=[]
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
a9=[]
with open('shrift.txt')as file:
    line=file.readline()
    s0=line
    line=file.readline()
    s1=line
    line=file.readline()
    s2=line
    line=file.readline()
    s3=line
    line=file.readline()
    s4=line
    line=file.readline()
    s5=line
    line=file.readline()
    s6=line
    line=file.readline()
    s7=line
    line=file.readline()
    s8=line
    line=file.readline()
    s9=line
a0=eval(s0)
a1=eval(s1)
a2=eval(s2)
a3=eval(s3)
a4=eval(s4)
a5=eval(s5)
a6=eval(s6)
a7=eval(s7)
a8=eval(s8)
a9=eval(s9)
z=input('Введите число: ')
a=[]
for i in range(len(z)):
    a.append(int(z[i]))
turtle.speed(10)
turtle.shape('turtle')
turtle.color('blue')
for l in range(len(a)):
    if a[l]==0:
        for i in a0:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==1:
        for i in a1:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==2:
        for i in a2:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==3:
        for i in a3:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==4:
        for i in a4:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==5:
        for i in a5:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==6:
        for i in a6:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==7:
        for i in a7:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==8:
        for i in a8:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])
    if a[l]==9:
        for i in a9:
            if i[2]==0:
                turtle.penup()
            else:
                turtle.pendown()
            turtle.forward(i[0])
            turtle.right(i[1])


        

