#####Numbers#######
print(3.14e-2)
print(123+222)
print(1.5*4)
print(2**100)
print(len(str(2**1000)))#if it is a very big number it converts a number into a string and it will give you the length of the string(not the answer) 
# len gives you the amount of characters in the string. A space would also be considered a character
import math
print(math.pi)
print(math.sqrt(85))
import random 
print(random.random())
random.choice([1, 2, 3, 4])
#########String########
print('''I'm "ok"''')
print('I\m learning\nPython.') # n makes it go to the next line
print('\\\n\\')
print(r'\\\t\\') # r is to avoid escape character
print('''line1...line2...line3''')
####Boolean###
True 
False 
print(3>2)
print(3>5)
True and True
True and False
False and False
print(5>3 or 1>3)
not True
not False
print(not 1>2)
age=21
if age >= 21:
    print('Yes, you can.')
else:
    print('Sorry.')

import time
print(time.time())
current= time.time()
second= current % 60
minutes= (current//60) % 60
hours = (current//60)//60 %24
days =(current//60//60//24)
print('Current time: %d days, %d hours, %d minutes and %d seconds from Epoch' % (days,hours, minutes, second))
input()