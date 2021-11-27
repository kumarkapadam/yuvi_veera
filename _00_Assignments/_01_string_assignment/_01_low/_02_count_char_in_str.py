# counting the number of character in string

"""
CRUD : retrieval
state : string
behaviour : for, while , == , += , <

"""

# ----- built in ------

name = 'shiva prasad'
count = name.count('a')
print('no of characters in a string', count)

# ----- algorithms -----

name = 'shiva prasad'
char = 'a'
res = 0
for i in name:
    if i == 'a':
        res += 1
print('no of characters in a string', res)

# ----- or ------

name = 'sai teja'
c = 'a'
res = 0
i = 0
while i < len(name):
    if name[i] == 'a':
        res += 1
    i += 1
print('no of characters in a string', res)

# ----- using function -----

n = 'sai teja'
c = 'a'


def count_char(name):
    r = 0
    k = 0
    while k < len(name):
        if name[k] == c:
            r += 1
        k += 1
    print('no of characters in a string', r)


count_char(n)
