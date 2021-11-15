# program to check whether a string starts with specified characters


'''
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  if else  for
'''

# 0. Mathematics 80%
'''
take a input as a string  and take a input as a another string(substring)
then comapare subsring to string 
its matches output is True not matches False


'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

str = input("enter any string :")

print(str.startswith('hello'))

# 2. Algorithm  80%

print("--------2. Algorithm----------")

str = input("enter any string")
start_with = input("enter start_with string")
for i in str.split():
    if i[0] == start_with:
        print("string start with ", start_with)
        break
else:
    print("string  not start with ", start_with)

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")

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
