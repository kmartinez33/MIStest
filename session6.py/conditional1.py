age = 20 
if age >=18:
    print('your age is', age)
    print('adult')

age= 12
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = int(input('how old are you?'))
if age >= 21:
    print('your age is{}'.format(age))
    print('your age is' + str(age)+ '.')
    print('yes, you can.')
elif age >= 6:
    print('your age is', age)
    print('you are a teenager. No, you cannot.')
else:
    print("your age is", age)
    print('no, not allowed.')

if age >= 6 and age <18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

######    Recursion   ######

def countdown(n):
    if n <= 0:
        print('Blastoff!!!')
    else:
        print(n)
        countdown(n-1)
countdown(5)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Hello', 3)

input()