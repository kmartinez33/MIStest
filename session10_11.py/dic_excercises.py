#### Excercise 1 ####

#def histogram(s):
    #d = dict()
    #for c in s:
        #d[c] = dict.get(c,0)
    #return d

#h = histogram('Bookeeper')
#print(h)


### Excercise 2 ###

def F(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return F(n-1)+F(n-2)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci (n-1) + fibonacci (n-2)
for i in range (1,10):
    print(fibonacci(i))

### Excercise 3 ###

# local known variables cannot be accessed from outside the function
#global variables can be written inside the function

#### Excercise 4 ####
flowers = ['Tulips', 'Tulips', 'Roses','Sunflower', 'Daisy', 'Orchid']

def has_duplicates(list):
    dict = {}
    for i in list:
        dict[i] = 1 + dict.get(i,0)
        if dict[i] > 1:
            return True
        else:
            return False
print(has_duplicates(flowers))
flowers = ['Tulips', 'Tulips', 'Roses','Sunflower', 'Daisy', 'Orchid']
