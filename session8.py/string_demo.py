team ='New England Patriots'
print(team[0])
# print (tema[1,5])

print(len(team))

print(team[len(team)-1])

last = team [-1]
print(last)

index= 0
while index< len(team):
    letter = team [index]
    print(letter)
    index +=1

for letter in team:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)

print(team[:11])
print(team[12:])

team[4:3]
team[::2]

team ='New England Patriots'
#team[12:20] = 'Seahawks'

new_team = team[:12]+'Seahawks'
print(new_team)
print(team)

####Searching###

def find(word, letter):
    index = 0 
    while index< len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E')) ### from New England ###

###Looping and counting###

word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

team = 'New England Patriots'
new_team = team.upper()
print(new_team)

team = 'New England Patriots'
index = team.find('a')
print(index)

print(team.find('En'))

print(team.find('a', 10))

name = 'bob'
print(name.find('b', 1, 2))

### The in Operator ###
'a' in team 
'Boston' in team

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)



input()