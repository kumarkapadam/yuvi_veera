# REQ : Find sum of 2 given numbers
"""
num1 = int(input("enter any number:"))
num2 = int(input("enter any number:"))  # num1,num2 variable


def sum(a, b):  # function signature a,b both are parameters
    # function body
    res = a + b  # behaviour
    print("sum of two numbers:", res)  # behaviour

# function calling
sum(num1, num2)
sum(10, 20)   # 10,20 arguments
sum(5, 10)    # 5,10 arguments
sum(-5, -10)  # -5,-10 arguments
sum(20, 40)   # 20,40 arguments



print("---------even numbers-----------")


def even_num(num):  # function signature # num is a parameter
# function body
    even = []
    odd  = []
    for i in range(1, num):  # behaviour
        if i % 2 == 0:  # logic # behaviour
            even.append(i)
        else:
            odd.append(i)
    print("even numbers:", even)
    print("odd numbers:", odd)


num = int(input("enter any number:"))  # state # user input
#  FUNCTION CALLING
even_num(num)  # num is arguments


import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)

"""



