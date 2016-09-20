import turtle
kathy = turtle.Turtle()
print(kathy)

kathy.fd(100)
kathy.fd(100)
kathy.lt(90)
kathy.fd(200)
kathy.lt(90)
kathy.fd(200)
kathy.lt(90)
kathy.fd(200)

for i in range(4):
    print('Hello!')
    
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

kathy= turtle.Turtle() #without this it just creates another square outside original square
square(kathy)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(kathy,150)

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(kathy, 6, 140) #the first number is the number of sides

bob = turtle.Turtle()
polygon(bob, n=6, length=70)

import math

def circle(t,r):
    circumference = 2 * math.pi * r
    n=80
    length = circumference / n 
    polygon(t,n,length)

circle(kathy, 35)

def circle(t,r):
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 1
    length = circumference / n
    polygon(t, n, length)

circle(bob,77)

def acr(t, r, angle):
    arc_length = 2* math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n 
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

acr(bob, 66, 180)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polyline(kathy, 2, 100, 180)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def acr(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

polygon(kathy, 5, 180)
acr(bob, 8, 280)

#def circle(t, r):
    #arc(t, r, 360)

#circle(kathy, 10)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polyline(kathy, 8, 120, 90)

turtle.mainloop()

