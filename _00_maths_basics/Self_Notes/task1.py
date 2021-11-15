str1 ="abc"
str2 ="defg"
list = []

for x,y in zip(str1,str2):
    list.append(x)
    list.append(y)
list.append(str2[-1])


print(list)
