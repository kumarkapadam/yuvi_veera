# Passing Arguments
'''
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)
'''
x = 10  # int x = 10

"""
# 1. Positional arguments (Required arguments)
print("--------1. Positional arguments--------------")

def sum(n1, n2, n3):   # sum(int n1, int n2, int n3) sum(int n1, String n2, List n3)
    print("In sum method : with vals :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20, 30)
sum(10+20, 20-3, 30*4)
a = 10
b = 20
c = 30
sum(a, b, c)



def stu_det(name,age,roll):
    print(f"student name is {name} age is {age} and roll number is{roll}")

stu_det('kumar',24,40)



def employee(name,id,location):
    print(f'employee name {name} id {id} and location is {location}')




name = input("enter employee name")
id = int(input("enter id"))
location =input("enter location")
employee(name,id,location)  





def sum(a,b,c):
    res = a + b + c
    print("sum is :",res)
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c= int(input("enter c number:"))
sum(a,b,c) 

print("--------------defaultarguments-----------------")
# default one argument
def stu_det(name,roll,college = 'JNTUH'):
    print(f'student name {name} roll number {roll},and college {college}')

stu_det('kumar',20)
stu_det('kiran',18,'SKU')


# default two arguuments

def stu_det(name,college ='jntuh',course ='pyhton'):
    print(f'student name {name} college is {college} course is {course}')

name = input("enter name:")    



print("---------marks grade----------")
def stu_det(name,roll,college="JNTUH"):
    print(f' name is .{name}\n roll number  {roll} \n,college name  {college} ')
    telegu = int(input("enter telugu marks:"))
    english = int(input("enter english marks:"))
    hindi = int(input("enter hindi marks:"))
    maths = int(input("enter maths maks:"))
    total = telegu + english + hindi + maths
    avg = total // 4
    if avg>0 and avg <100:
        if avg>90:
            print("A grade")
        elif avg >70:
            print("b grade")
        elif avg >50:
            print("c grade")
        else:
            print('fail')
#stu_det('kumar',10)
stu_det('kiran',18,'sku')   

print("------------------keyword arguments-------------------")
def sum(a,b,c):
    res = a+b+c
    print("the sum of the numbers:",res)
sum(a=10,c=20,b=15)
sum(a=8,b=2,c=15)
sum(10,20,40)
sum(c=3,a=2,b=10)
sum(10,c=10,b=5)

string=input("Enter string:")
word=input("Enter word:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count) """










