# P01 Req: sum of the elements in a list


'''
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->    |  =   +=    |   for
'''

# 0. Mathematics 80%
'''
1. Define the list
2. Take initial sum as 0
3. Start reading it. 
4. While reading each char, sum of the elements
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

list = [10,20,30,40,50]  # static way
# message = input("Enter any string : ")

print("sum of the list : ", sum(list))


# 2. Algorithm  80%

print("--------2. Algorithm----------")

list = [10,20,30,40,50]
sum = 0
for i in list:
    sum +=i
print("sum of the list is:",sum)

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
