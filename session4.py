print(type('42'))
int('42')
int(3.99)
int(-2.3)
float(76)
float('3.14')
str(87)
str(31.54)
abs(-1299)
max(1,2)
max(43,3838,-338,-3988)

chr(ord('A')+32)
ord('a') - ord('A')
ord('b') - ord('B')
len('Aryan') #len=how many characters it has
pow(3,3) # 3 to the power of 3
round(4.1)

import math
ratio=100
math.log10(ratio)

def print_lyrics():
    print("Hey Jude.Dont.")
    print("take a sad song.")

print(type(print_lyrics))
print_lyrics()

def repeat_lyrics():
    print('na-na-na-na, na-na-na')
    print_lyrics

print(repeat_lyrics())

def print_twice(a):
    print(a)
    print(a)

def cat_twice(part1, part2):
    cat= part1+part2
    print_twice(cat)

line1 = 'Bing tiddle'
line2 = 'tiddle bang'
#cat_twice(line1, line2)

def give_me_a_break():
    str1 = 'break'
    print('another break')
    return str1
print(give_me_a_break())

def a_new_function_demo():
    s=0
    for x in 'Chris':
        print(x)
        print(ord(x))
        s = s + ord(x)
 
 #print(a_new_function_demo())

 def my_abs(n):
     if n > = 0:
         return n
     else:
         return -n

print(my_abs(100))
print(my_abs(-4))
print(my_abs(7))


input()