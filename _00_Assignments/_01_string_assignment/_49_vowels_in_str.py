# count and display the vowels of a given text
# P01. REQ : Find length of given string   ie., "Hello World"

'''
1. CRUD       -retrieve
2. STATE      - string / input()
3. BEHAVIOR   - + operator / for loop
'''
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics 80%
'''
1. Define the string, ant store the vowels in list ,and 
2. Take initial count as 0
3. Start reading it. 
4. While reading each char, increase the key count 
'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")



# 2. Algorithm  80%

print("--------2. Algorithm----------")

str = input("enter any string:")
list = ['a','e','i','o','u']
count = 0
dict = {}
for i in str:
    if i in list:
        if i in dict:
          dict[i]+=1
        else:
            dict[i]=1
print(dict)



# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")
def vowels_str(str):

    list = ['a','e','i','o','u']
    count = 0
    dict = {}
    for i in str:
        if i in list:
            if i in dict:
              dict[i]+=1
            else:
                dict[i]=1
    return dict

str = input("enter any string:")
vow = vowels_str(str)
print("vowels in strings ",vow)




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
