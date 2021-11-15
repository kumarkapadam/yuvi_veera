# https://docs.python.org/3/library/exceptions.html
""""""
'''
BaseException
 +-- Exception
      +-- ArithmeticError+
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      +-- RuntimeError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError

           '''

"""try:
    num1 = int(input("enter any number :"))
    num2 = int(input("enter any number :"))
    num3 = num1 / num2
    print(" division   :",num3)   # only try block will not execute ,except except block or finally block.
"""
try:
    num1 = int(input("enter any number :"))
    num2 = int(input("enter any number :"))
    num3 = num1 / num2
    print(" division   :", num3)

except ValueError:
    print("please enter integer numbers only")
except ZeroDivisionError:
    print("you enter b value is zero ")
    print("please enter positive value")

except Exception as e:
    print("error occurred ==", type(e))

print("**************************  key error   ****************************")

"""
dict1 = {'name': 'kumar', 'id': 27, 'loc': 'hyd'}
print("normal dictionary  :",dict1)
print("name :",dict1['name'])
print("company is :",dict1['company'])  # KeyError  """

try:
    dict1 = {'name': 'kumar', 'id': 27, 'loc': 'hyd'}
    print("normal dictionary  :", dict1)
    print("name :", dict1['name'])
    print("company is :", dict1['company'])
except KeyError as ke:
    print("key is not found in dictionary")

print(" ***********************  indentation error  *************************")

"""def add(x,y):

z=x+y    # indentation error
print("z value :",z)

add(10,20) """

print(" ***********************   value error  *****************************")

try:
    x = int(input("enter any number :"))
    print('x value is :', x)

except ValueError:
    print("please enter integers only")

pre_year = input("enter present year:")
birth_year = input("enter your birth year")

age = pre_year - birth_year
print(age)  # TypeError: unsupported operand type(s) for -: 'str' and 'str' """

print(" **************************  type error **************************")
try:
    pre_year = input("enter present year:")
    birth_year = input("enter birth year")
    age = pre_year - birth_year
except TypeError as ve:
    print("please enter integer type only")
    print("TypeError: unsupported operand type(s) for -: 'str' and 'str'", ve)
except Exception:
    print("exception occurred")
finally:
    print("end_program")

print("************************  zero division error ************************")

try:
    num1 = int(input("enter any number "))
    num2 = int(input("enter any number "))
    num3 = num1 / num2
    print("division is :", num3)
except ZeroDivisionError as zde:
    print("please enter denominator other than zero ")
except Exception:
    print(" error occurred ")
