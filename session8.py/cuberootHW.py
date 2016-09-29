x = int(input('Enter an integer: '))
ans = 0
while ans**3 == abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans)) 


cube = 27 
for guess in range(abs(cube)+1):