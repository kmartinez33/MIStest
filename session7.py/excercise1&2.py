#### E.1####
result = 0
for i in range(11): #would change to 11 so that it actually counts the 10
    result +=i
print (result)
print(1+2+3+4+5+6+7+8+9+10)

### E.2 #####

result = 0
for i in range(1,11,2): #would change to 11 so that it actually counts the 10
    print('Current i:', i)
    result +=i
print (result)
print(1+2+3+4+5+6+7+8+9+10)

def countdown(n):
    while n>0:
        print(n)
        n = n -1
    print('Blastoff!')

countdown(5)

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

    iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


result = 0 
i = 1
while i< 11:
    if i %2 ==0:
        result = result +i
    i= i+1 # always raise the i

print(result)

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')

mysum = 0 
for i in range(5,11,2):
    mysum += i
    if mysum == 5:
        break
print(mysum)


input()
