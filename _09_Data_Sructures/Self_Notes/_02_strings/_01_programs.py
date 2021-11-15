"""print("---------string using for loop----------------")
str = "hello kumar"
print("string is:",str)
for i in  str:
    print(i , end =" ")
print()

print("----------string using while loop0------------")
i=0
n = len(str)
while i<n:
    print(str[i],end = " ")
    i+=1
print()

print("----------string using while loop0------------")
i=-1
n = len(str)
while i>=-n:
    print(str[i],end = " ")
    i-=1
print()

print("----------string using while loop0------------")
i=1
n = len(str)
while i<=n:
    print(str[-i],end = " ")
    i+=1
print()

print("--------------whether substring exists in main string------------")

string = 'hello  welocme to the python programming language'
sub =input("enter any string")
if sub in string:
    print("substring exists in string")
else:
    print("not existing")

print('-----------comparing strings----------------')

str1 = input("enter any string:")
str2 = input("enter another string:")
if str1 == str2:
    print("both are same")
else:
    print("not same ")


str1 = '  kumar  '
str2 ='kumar'
if str1.strip() == str2:
    print("both same")
else:
    print("not same")

print("--------find the first occurrence of sub strong in a given string----------")

string = input("enter any string")
sub = input("enter substring")

n=string.find(sub,0,len(string))
if n == -1:
    print("not found")
else:
    print("found",n+1) """

print("------python program display all positions of sub string-------")

"""str = input("enter any string:")
sub = input("enter sub string:")

i=0
n = len(str)
flag = False
while i<n:
    pos = str.find(sub,i,n)
    if pos == -1:

        i+=1
    else:
        print('found',pos+1)
        i = pos +1
        flag = True
else:
    if flag == False:
        print("not found") 

string = input("enter any string:")
sub = input("enter any substring")

for i in string:
    if i == sub:
        print("found",string.index(i))
       
        
       
        break
else:
    print("not found")


string = input("enter any string :")
sub = input("enter any sub string:")

n = len(string)
i =0
flag = False
while i < n:
    pos = string.find(sub,i,n)
    print("pos",pos)
    if pos != -1:
        print('fpund',pos + 1)
        i = pos + 1
        flag = True
    else:
        i+=1

else:
    if flag == False:
        print("not found")

str = []
num = int(input("enter how many strings inserted:"))
for i in range(num):
    elem = input("enter string")
    str.append(elem)
print("strings",str)
print(str)
# sorted strigns
str1 = sorted(str)
for i in str1:
    print(i)
"""
str = input("enter any string :")

len = 0
for i in str:
    print(str[len],end="  ")
    len+=1

print("\nlength of the string:",len)
























