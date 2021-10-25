# membership operator:


"""
membership operator are used test if a sequence is presented in an object
in:>> returns true
if a sequence with the specified value is present in the object

not in --->>> returns true
 if a sequence with the specified value is not present in the objerct
"""

"""list =[1,2,4,45,6]
list1=[1,2,4,45,6]
list2 = list
print(list is list1)
print(list is list2)

num =[2,4,6,1,9,5]
for i in num:
   if i%20==0:
       print(i) """

list = [1, 2, 3, 4, 5, 6]
print(1 in list)  # True
print('2' in list)  # False
print("kumar" in list)  # False
print("kumar" not in list)  # True

print('k' in ['k', 'u', 'm', 'a', 'r'])  # true
print('K' in ['k', 'u', 'm', 'a', 'r'])  # False

"""list =[1,2,4,5,65]
for i in enumerate(list,start=1):
    print(i) """

str1 = 'Hello World'
list1 = [1, 2, 3, 4, 5, 6]
tup1 = (1, 2, 3, 4, 5, 6)
dict1 = {1: 1, 2: 2, 3: 3}
set1 = {1, 2, 3, 4, 5, 6}

# in not in

print(1 in list1)
print(8 not in tup1)
print(8 not in dict1)
print(6 in set1)
print(7 not in set1)
print(10 in set1)
