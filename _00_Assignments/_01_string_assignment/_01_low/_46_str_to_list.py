# convert string in a list

'''
1. CRUD       -update
2. STATE      - string / input()
3. BEHAVIOR   -  for loop
'''

# 0. Mathematics
'''
take a input string
then append to the list
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

str = 'hello kumar'
s = str.split(" ")
print(s)
print(type(s))

# 2. Algorithm  80%


str = input("enter any string:")
list = []
for i in str:
    print(i)
    list.append(i)
print(list)

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")


def str_to_list(str):
    list = []
    for i in str:
        print(i)
        list.append(i)
    return list


str = input("enter any string:")
convert = str_to_list(str)
print("convert string to list:", convert)

# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")

# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")

# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
