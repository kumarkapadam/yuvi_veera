a = int(input("enter a number"))
b = int(input("enter b number"))
c = a + b
print("addition of two numbers", c)


def add():
    x = int(input("enter a number:"))
    y = int(input("enter b number:"))
    z = x + y
    print(" z value    :", z)


add()

for i in range(ord('a'), ord('z') + 1):
    print(chr(i))

import pdb


def trans(a, b):
    z = a + b
    print("addition of two numbers", z)


pdb.set_trace()
x = 10
y = 20
trans(x, y)

"""
# debugging at command lines

n  -         execute next line
c            complete execution
l            list 3 lines before and after current line
s            step into function call
b            show list of all break points
b[int]       set break point at line number
b(func)      break at function name
cl           clear all break points
cl[int]      clear break point at line number
p            print()

"""

# n  -         execute next line
import pdb

list = [10, 20, 30, 50, 60, 70]
print("list is :", list)
pdb.set_trace()
for i in list:
    print(i)



# c        complete execution


list1 = [10, 11, 1, 2, 3, 4, 5, 7, 8]
pdb.set_trace()
for i in list1:
    print(i)

# l      list 3 lines before and after current line  

import pdb

list = []
num = int(input("enter how many numbers to be inserted "))
for i in range(num):
    pdb.set_trace()

    elem = int(input("enter number  "))
    list.append(elem)
print("normal list is", list)

# b        show list of all break points
import pdb

for i in range(1, 20):
    if i % 2 == 0:
        pdb.set_trace()
        if i == 8:
            break
    print(i)
