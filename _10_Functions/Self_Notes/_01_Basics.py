# BUilt_in_Functions

"""The Python built-in functions are defined as the functions whose functionality is pre-defined in Python.
 The python interpreter has several functions that are always present for use.
 These functions are known as Built-in Functions   """

"""print("----------addition of two numbers------------")

a = int(input("enter a number:"))  # state  # input
b = int(input("enter b number:"))  # state  # input

res = a + b  # business logic

print("addition of a and b is", res)  # give response to user

# using user-defined function


The four steps to defining a function in Python are the following:

Use the keyword def to declare the function and follow this up with the function name.
Add parameters to the function: they should be within the parentheses of the function. End your line with a colon.
Add statements that the functions should execute.
End your function with a return statement if the function should output something. Without the return statement, your function will return an object None.

"""

print("-------------using functions---------------")

num1 = int(input("enter any  number:"))  # input # static
num2 = int(input("enter any number:"))  # input  # static

def sum(a, b):  # here a and b are parameters
    res = a + b  # behaviour
    return res  # return the result


s1 = sum(num1, num2)  # here num1 and num2 are arguments
print("addition of two numbers :", s1)  # behaviour # print the result




def sum(a,b):
    res = a+b
    print("addition of a and b ",res)

a=10
b=20
sum(a,b)
sum(10+20,30)       # (30,30)    #60
sum(30-10,20-10)    # (20,10)    #30
sum(10*2 + 3*6,10)  # (20+18,10) #48





def sum(x, y):  # function defining
    # function body
    res = x + y  # Business logic
    print("addition of a and b ".ljust(10, '-'), ":", res)  # print the result


sum(10, 20)
sum(10, 0)
sum(10, -5)
sum(-3, -2)
sum(-3, 0)
sum(-2, 10)













