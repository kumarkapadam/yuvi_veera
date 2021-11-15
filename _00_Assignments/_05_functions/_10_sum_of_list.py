'''
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->   for
'''


def sum(list):
    sum =0
    for i in list:
        sum+=i
    return sum
list = [10,20,30,50,60]
"""
list1 =[]
num = int(input("enter how many numbers to be inserted"))
for i in range(num):
    elem = int(input("enter number:"))
    list1.append(elem)
print(list1)
    
s=sum(list)
print("sum of all the elements in list:",s)

"""