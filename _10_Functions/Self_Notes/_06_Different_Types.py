# Function categories

"""
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type """

"""

print("--------Function with parameters, with return type------------")

num1  = int(input("enter any number :"))  # state
num2  = int(input("enter any number :"))  # state
def sum(num1,num2):
    result  = num1 + num2
    return result
s1 = sum(num1,num2)
print("addition of two numbers  is ",s1)


print("----------------------even number------------------")
even = []
odd=[]
def even_num(num):

    for i in range(1,num):
        if i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd



num = int(input("enter any number"))
ev = even_num(num)
print("even numbers :",even)
print("odd numbers :",odd) 


print("-----------with parameters without return type-----------")


def sum1(a,b):
    res = a+b
    print("addition of a and b is",res)

a = int(input('enter a number :'))
b = int(input("enter b number :"))
sum1(a,b)
sum1(10,20)
sum1(-10,7)
sum1(10*2,10+3)



def even(num):
    even1 = []
    for i in range(1,num):
        if i%2==0:
            even1.append(i)
        print("even numbers",even1)


num = int(input("enter any number:"))
even(num)  """

# without parameter and with return type
print("-------------------way1-------------------------")
def sum():
    a=int(input("enter any number:"))
    b=int(input("enter b number:"))
    res = a+b
    return res

print("sum of two numbers is:",sum())

print("----------------way2----------------------------")

def sum():
    a=int(input("enter any number:"))
    b=int(input("enter b number:"))
    res = a+b
    return res

sm = sum()
print("sum of two numbers is:",sm)





print("----------without parameter and without  return type----------")
def sum():
    x= int(input("enter any number:"))
    y= int(input("enter any number:"))
    res = x+y
    print("sum of x and y is:",res)
sum()