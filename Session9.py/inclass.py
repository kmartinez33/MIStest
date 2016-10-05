fin = open('words.txt')
line = repr(fin.readline())

print(line)

#fin = open('words.txt') #this opens all the words so it freezes bc there are so many
#for line in fin:
    #word = line.strip()
    #print(word)

line = fin.readline()
word = line.strip()

print(word)

def long_words():
    """
    prints only the words with more than 20 characters
    """
    fin = open ('words.txt')
    for line in fin:
        word = line.strip()
        if len(word)>20:
            print(word)
long_words()

def has_no_e(word):

#returns True if the given word doesn’t have the letter “e” in it.
 
    for letter in word:
        if letter == 'e':
            return False
        return True

print(has_no_e('Babson'))
print(has_no_e('College'))

def avoids(word, forbidden):

    #takes a word and a string of forbidden letters, and that returns True
    #if the word doesn’t use any of the forbidden letters.
    for letter in word:
        if letter in forbidden:
            return False
        return True

print(avoids('Babson', 'ab')) #going to return Treu because ab is in Babson
print(avoids('College', 'ab'))

def uses_only(word, available):

#takes a word and a string of letters, and that returns True if the word
#contains only letters in the list.
    for letter in word:
        if letter not in available:
            return False
    return True

print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('College', 'aBbsonxyz'))

def uses_all(word, required):

# takes a word and a string of required letters, and that returns True if
# the word uses all the required letters at least once.
    for letter in required:
        if letter not in word:
            return False
    return True

# or since statement is same you can use function above
#return def uses_only(required,word):

print(avoids('Babson', 'ab')) 
print(avoids('College', 'ab'))

def is_abecedarian(word):

#returns True if the letters in a word appear in alphabetical order
#(double letters are ok).
    before = word[0]
    for letter in word:
        if letter<before:
            return False
        before = letter
    return True

pritn(is_abecedarian('abs'))
print(is_abecedarian('college'))


input()