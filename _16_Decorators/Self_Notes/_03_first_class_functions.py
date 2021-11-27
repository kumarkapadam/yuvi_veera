'''
@classmethod
@staticmethod

Decorator : Provides additional functionality for class or method/function
'''

''' 
#1 one time usage
print(10)

# 2 or more places
x = 10  
print(x)         XXX ---> print(10)
print(x+100)     XXX ---> print(10+100)
'''
"""
print(" multiple decorators in single function")

def upper_decorator(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner
def split(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split
@upper_decorator
def ordinary():
    return 'hello hai'
print(ordinary())






# decorator countain parameter
def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr
        return inner()
    return upper_d

@outer("kumar")
def ordinary():
    return "hai hello"
print(ordinary())



def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner()


def str_lower(func1):
    def lower1():
        str1 = func1()
        return str1.lower()

    return lower1()


@str_lower
@str_upper
def great():
    return "good morning"


print(great)




def check_name(method):
    def inner(name_ref):
        if name_ref.name == "kumar":
            print("same name")
        else:
            method(name_ref)
    return inner

class printing:
    def __init__(self,name):
        self.name = name
    @check_name
    def print_name(self):
        print("entered user name is:",self.name)

pr = printing("kumar")
pr.print_name() 
"""

print(" ****************   __call__()   ****************")
class Printing():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __call__(self):
        print(f'name is {self.name} and age is {self.age}')

p = Printing('kumar',24)
p()







class Decorator:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        str1 =self.func()
        return str1.upper()
@Decorator
def greet():
    return "good morning"
print(greet())