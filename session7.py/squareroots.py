a = 4
x = 3
y = (x+a/x) / 2
print(y)
 
x = y 
y = (x +a/x)/2
print(y)

x=y
y=(x+a/x)/2
print(y)

x=y
y=(x+a/x)/2
print(y)

x= y ###stops when the estimate is almost exact
y=(x+a/x)/2
print(y)

while True:
    print(x)
    y =(x+a/x)/2
    if y==x:
        break
    x=y

#if abs(y-x) < epsilon:
    #break

input()