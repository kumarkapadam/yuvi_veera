# list is empty
print("-----------------------list is empty-------------------------")
data = []
print("empty list is",data)  #empty list is []
print(type(data))     #<class 'list'>

print("---------------------list inside numbers(integer)(float)-----------------------")

#list inside integer
data=[1]
print("list inside integer:",data) #integer value inside the list: [1]
print("type of the list is:",type(data)) # type of the list is: <class 'list'>

#list inside float

data =[20.98]
print("list inside float:",data)
print(type(data))

#list inside string

data =['kumar']
print("list inside string",data)
print(type(data))

#collection of datatypes inside the list
data1 =[1,1.9,'kumar','23',20.98]
print(data1)

data1 =[1,2,3,(3,4,5),{1,3,4},{'one':1,"two":2}]
print(data1[1])
print(data1)
a=data1[3]
b=list(a)
b.append(10)
print(b)
print(data1)


"""a=1,2,3
print(type(a))
print(list(a))
b=list(a)
b.append(5)
print(b) """


