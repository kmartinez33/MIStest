[10, 20, 30, 40]
['New England Patriots', 'Buffalo Bills','Miami Dolphins','New York Jets']

['spam', 2.0, 5, [10,20]]
AFC_east = ['New England Patriots', 'Buffalo Bills','Miami Dolphins','New York Jets']
numbers = [42, 123]
empty= []
print(AFC_east,numbers, empty)

AFC_east[3] = 'New York Giants' #New england is at 0 so 3 is new York jets. this is changing the jets part to giants by just using 3 bc it is in a list
print(AFC_east)

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print('Buffalo Bills' in AFC_east)
 ###Excercise 1####
#L = [
   # ['Apple', 'Google', 'Microsoft'],
   # ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
   # ['Adam', 'Bart', 'Lisa']
   # ]

###traversing a list####

for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i]= numbers[i] * 2

print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] * 4
['Tom Brady', 'Bille Belchick']*3

t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t[1:3])

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y'] # 1 to 3 is a range so it will go up to the third one but not include the 3rd one
print(t)

###Excercise 2####

t = ['a', 'b', 'c']
t.append('d')
print(t)

input()
