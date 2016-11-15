import math

x = float(input())
if x > 0:
    y = math.log(x)
else:
    y = float('nan') # a special floating-point value that represents “Not a Number”. 
print(y)

y = math.log(x) if x > 0 else float('nan')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# conditional expression
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

input()
