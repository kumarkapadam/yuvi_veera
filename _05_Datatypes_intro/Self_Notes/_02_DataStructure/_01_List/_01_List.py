"""list=[10,20,10.5,"kumar",True,[1,2,3,4],(5,6,56),{10,111,123},{1:"one"},{2:"two"}]
print(list) """
"""
list built in functions
1.append
2.extend
3.insert
4.index
5.pop
6.remove
7.copy
"""

#---------------------append AND extend---------------------
list=[]
list.append(1)
print(list)     # [1]
list.append([2,4,5])
print(list) #[1, [2, 4, 5]]
list.extend([10,15,16])
print(list) #[1, [2, 4, 5], 10, 15, 16]
list.append('kumar')
list.append(20.01)
print(list) #[1, [2, 4, 5], 10, 15, 16, 'kumar', 20.01]


#-------------pop------------------
#pop we can use its remove the last element and also we can use the index
print(list.pop()) #20.01
print(list.pop(2)) #10

print(list.remove(15)) #15
print(list) #[1, [2, 4, 5], 16, 'kumar']

print(list.insert(0,11))
print(list) #[11, 1, [2, 4, 5], 16, 'kumar']

print(list.reverse())
print(list) #['kumar', 16, [2, 4, 5], 1, 11]

print(list.count(1))#1
#------------------indexing------------------------------
x=[1,2,3,4,5]
print("before indexing",x) # before indexing [1, 2, 3, 4, 5]
print(x[3]) #4
x[3]=10
print("after indexing",x) #after indexing [1, 2, 3, 10, 5]

print("indexing of ",x.index(3)) #indexing of  2


