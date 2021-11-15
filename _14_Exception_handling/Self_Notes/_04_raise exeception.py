
print("---------------raise exceptions---------------")
try:
    amt = 1000
    if amt < 5000:
        raise NameError("Insuff. Funds")  # Raise exception manually
    print("Fund transfer completed successfully")
except NameError as name:
    print("AN EXCEPTION OCCURED ::", name)

print("---------------raise exceptions---------------")
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
    print("positive number :", a)
except ValueError as ve:
    print(ve)

print("---------------raise exception---------------")

try:
    num = int(input(" enter any number :"))
    if num >= 0:
        if num == 0:
            print("zero")
        else:
            print(num, "is positive number")
    else:
        print(num, " is negative number")
except ValueError as ve:
    print("please enter integer number")
except Exception as e:
    print("error occurred ")
finally:
    print("end")



try:

    x = int(input("enter number"))
    if x <= 0:
        raise ValueError(
            "Only positive numbers are allowed")  # here i am throwing exception manually
    if type(x) != int:
        raise TypeError("Type Error")  # here i am throwing exception manually
    print("x value :", x)
except Exception as e:
    print("Exception occurred :: ", e)

print("------------------------------------")

try:
    num = int(input("enter a number:"))
    print(num)
except:
    print("exception occurred")
finally:
    print("end")

try:
    list = []
    num = int(input("how many  numbers inserted in list:"))
    for i in range(num):
        elem = int(input("enter number:"))
        list.append(elem)
    print("list is :",list)
except ValueError:
    print("enter only integer number ")
finally:
    print(" end ")






try:
    age = int(input("enter your age"))
    if age < 0:
        raise ValueError("please enter positive number only")
    elif age>100:
        raise OverflowError("please enter below 100 only ")
    elif age > 18:
        print("eligible for vote")

except OverflowError as e:
    print(e)
except ValueError as e:
    print(e)

except Exception as e:
    print("exception occurred ")
else:
    print("executed successfully")
finally:
    print("end_program")































