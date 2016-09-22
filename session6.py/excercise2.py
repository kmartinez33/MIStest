def factorial(n):
    if n ==1:
        return 1 
    return n * factorial(n-1) #replace result= with return and it will be the same

print(factorial(1))
print(factorial(3))
print(factorial(4))
print(factorial(8))

def fib(n):
    if n ==1 or n ==2:
        return 1
    return fib(n-1)+ fib(n-2)

print(fib(3))
print(fib(10))

#####eXCERCISE 2.3 greatest common divsor #####

def gcd(a, b):
    if b == 0:
       return a
    else:
        return gcd(b, a % b)  #% is module

print(gcd(2,12))
print(gcd(10,40))
print(gcd(15,80))
print(gcd(80,15))

### excercise 2.4 ###

def move(n, source, bridge, destination):
    if n <= 0:
        return
    else:
        move(n-1, source, bridge, destination)
        print(source, destination)
        move(n-1, bridge, destination, source)
 
move(3,'A', 'B', 'C')


input()
