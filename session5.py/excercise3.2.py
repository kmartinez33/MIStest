import turtle
import math
dragon = turtle.Turtle()
print(dragon)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

import math

def circle(t,r):
    circumference = 2 * math.pi * r
    n=50
    length = circumference / n 
    polygon(t,n,length)

circle(dragon, 79)

def move(t,xpos,ypos):
    t.pu() #moves it without the line
    t.setx(xpos)
    t.sety(ypos)
    t.pd() #moves it without the line

move(dragon,5.5,80.5)


def petal(t, r, angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def mpetal(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.right(360.0/n)

mpetal(dragon, 6, 60, 80)

turtle.mainloop()