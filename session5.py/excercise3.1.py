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

def tri(t, angle):
    for i in range(2):
         t.right(angle)
         t.lt(30)
         t.fd(200)
         t.rt(120)
         t.fd(200)
         t.rt(120)
         t.fd(400)
         t.lt(120)
         t.fd(200)
         t.lt(120)
         t.fd(200)
    
tri(dragon, 120)

dragon.fd(205)
dragon.lt(90)
dragon.circle(205)
dragon.lt(90)
dragon.fd(120)
dragon.circle(50)
dragon.fd(135)
dragon.right(140)
dragon.circle(45)

dragon.rt(40)
dragon.fd(100)
dragon.lt(90)
dragon.circle(50)



turtle.mainloop()