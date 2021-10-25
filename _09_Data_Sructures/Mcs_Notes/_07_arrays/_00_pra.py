"""# 1 to 10

for i in range(11):
    print(i)

list = [1,2,3,4,5,6,7]
for index,value in enumerate(list):
    print(f'index of {index}',value)



i=10
while(i>0):
    i-=1
    print(i)

list1 =len(list)
i = 0
while(list1>0):
    print(f'index of {i-1} is',list[i-1])
    list1-= 1
    i-=1


# 1 to 10

for i in range(1,10):
    print(i)

# 10 to 1

num = 10
while(num>0):
    num-=1
    print(num)



list = [1, 2, 3, 4, 5]
for index, value in enumerate(list):
    print(f'index of {index} is', value)
    if list[4] == 5:
        list[4] = 10
        print(list)
        if True:
            list.extend([10,11,12])
            print("extended list ",list)


num = int(input("enter how many numbers to be inserted:"))
list = []
print(num)
for i in range(num):
    elem = int(input("enter number"))
    list.append(elem)
print(list)

sum = 0
list = [12,19,20,21]
for i in list:
    sum+=i
    print(sum)

num  = int(input("enter how many numbers to be inserted :"))
list = []
sum = 0
for i in range(num):
    elem = int(input("enter number:"))
    list.append(elem)
print(list)
for j in list:
    sum+=j
print(sum)
avg = sum//num
print(avg)

a = int(input("enter a number:"))
b = int(input("enter b number:"))
c=[]
c.append(a)
c.append(b)
for i in range(0,2):
    for j in range(0,2):
        if i !=j and j != i:

num = 1234
sum = 0
while(num>0):
    dig = num % 10
    sum = sum + dig
    num = num // 10
print(sum)


num = int(input("enter any number:"))
temp = num
rev = 0
while (num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if temp == rev:
    print("polindrome")
else:
    print("not ")

num = int(input("enter how many numbers to be inserted :"))
list = []
for i in range(num):
    elem = int(input("enter number:"))
    list.append(elem)
print(list)
even_sum = 0
odd_sum = 0
neg_sum =0
for j in list:
    if j%2==0:
        print(j)
        even_sum +=j
    else:
        print(j)
        odd_sum+=j
else:
    neg_sum+=j

print(even_sum)


num =10
list =[]
for i in range(num):
    print(i ,sep=" ",end=" ")
    list.append(i)
    if i<num-1:
        print("+",end=' ')
print("=",sum(list))

even = []
odd = []
even1= 0
odd1=0
for i in range(100):
    if i %2 == 0:
        #print(i)
        even.append(i)
        even1+=i
    else:
        #print(i)
        odd.append(i)
        odd1+=i
print("evene  numbers",even)
print("odd numbers",odd)
print("sum of even numbers",even1)
print("sum of add numbers",odd1)
"""

list1 = []
ls=[]
num = int(input("enter numbers to  be inserted:"))
for i in range(num):
    elem = int(input("enter number"))
    list1.append(elem)
print("list is :",list1)
list1.sort()
print("largest number is",list1[-1])
for i in list1:
    print(j)
    if j not in i:
        print(j)
        ls.append(j)
print(ls)