import turtle
jerry = turtle.Turtle()
print(jerry)
def square(t, length):
    t.fd=(length)
    t.lt(90)
    t.fd=(length)
    t.lt(90)
    t.fd=(length)
    t.lt(90)
    t.fd=(length)
  #print(t)

jerry= turtle.Turtle()
square(jerry,100)

kathy= turtle.Turtle()
square(kathy,250)


turtle.mainloop()
