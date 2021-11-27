'''
A decorator that allows a user to add new functionality to an existing object without
modifying its structure.
Decorators are usually called before the definition of a function you want to decorate.

This means that they support operations such as being passed as an argument,
returned from a function, modified, and assigned to a variable.

1.need to take a function as parameter
2.add functionality to the function
3.functionneed to return another function


'''


# assigning function to variable

def add(x, y):
    z = x + y
    return z


add(10, 5)
print("addition of two numbers is:", add(10, 5))

print(" ***************   function inside another function  **********")


def hello_function():
    def say_hi():
        return "Hi"

    return say_hi


hello = hello_function()
print("Return other function:", hello())


def outer_function():
    message = 'hello kumar'
    print("outer function message :", message)

    def inner_funtion():
        print("inner function message:", message)

    return inner_funtion()


outer_function()

print("*****************************************************")


def add_fun():
    x = 10
    y = 15

    def sum():
        z = x + y
        print(z)

    return sum()


add_fun()
add_fun()

print("   *********  using argument  ********")


def outer_fun(msg):
    message = msg

    def inner_fun():
        print(message)

    return inner_fun()


outer_fun("hai kumar how are you")
outer_fun("hai")

print(" ************       sum of the numbers  ************************ ")


def sum(x, y):
    z = x + y

    def add():
        print("additon is :", z)

    return add()


sum(10, 23)
sum(0, 10)
sum(10, 0)
sum(23, 12)

print(" ***********************   ********************  *********************")


def fun_msg(message):
    def inner_msg():
        return message

    return inner_msg()


msg = fun_msg('hello yuvi')
print(msg)

print(" ***********************   adding ***********************")

"""
def add_out_fun(x,y):
    def add_in_fun(x,y):
        z=x+y
        return z
    return add_in_fun()
def display():
    print("addition of two numbers:",add_out_fun)

add_out_fun(10,20)
"""

print(" **********     div   **************")


def div(x, y):
    z = x / y
    print(f'divisible by {x}/{y}:', z)


def smart_div(func):
    def inner(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)

    return inner


div1 = smart_div(div)
div1(2, 4)

print(" ************   upper_decorator ******************")


def upper_decorator():
    def inner_upper():
        msg = input("enter any message :")
        x = msg.upper()
        print("normal message is :", msg)
        print("x is using upper method :", x)

    return inner_upper()


upper_decorator()

"""
def upper_decorator():
    def inner_upper():
        msg = input("enter any message :")
        x = msg.upper()
        return x,msg
    return inner_upper()

upper_decorator()
print(upper_decorator())



def normal_string():
    def upper_string():
        upp = msg.upper()
        return upp

    return upper_string()


def str_msg():
    msg = input("enter any  string:")
    return msg

str1 = normal_string(str_msg)
print(str1())  """

'''
any callable python object that is used to modify a function or class
'''

print(" *********** nested function ***********")


def outer():
    x = 10

    def inner():
        y = 3
        result = x + y
        return result

    return inner()


a = outer()
print(a)


def function1():
    print("hello ,  this is function1")


def function2(func):
    print("hi i am function2 now i will call function1")


function2(function1)

print("*****************   ***************   *******************")


def str_upper(func):
    def inner():
        # str1 = print_str()
        str1 = func()
        return str1.upper()

    return inner


def print_str():
    return "good morning"


print(print_str())
d = str_upper(print_str())
print(d())

print(" *************************************")


def str_upper(func):
    def inner():
        # str1 = print_str()
        str1 = func()
        return str1.upper()

    return inner


@str_upper
def print_str():
    return "good morning"


print(print_str())

print("          *******************************     ")


def dic_decorator(func):
    def inner(x, y):
        if y == 0:
            return "give proper input"
        return func(x, y)


def div(a, b):
    return a / b


print(div(10, 0))

print(" ********************  ")


def outer(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner()


@outer
def print_str():
    return "hello "


print(print_str)
