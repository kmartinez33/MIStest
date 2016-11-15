a = 'Babson College'
b = [e.upper() for e in a]
b2 = [e.upper() for e in a if e in 'aoeiu']
#those letters in upper case that are vouels 

a2 = 'Babson College is cool'
b3 = [e.upper() for e in a.split()]
print(b3)

a = 'Babson College is a great school'
b = [e.upper() for e in a.strip()]
print(b)

b = [e.upper() for e in a.split()]
print(b)
