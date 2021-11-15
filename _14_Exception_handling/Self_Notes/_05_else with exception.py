"""
def get_num(x, y):
    try:
        x = int(input('enter x number:'))
        y = int(input("enter y number:"))

    except ZeroDivisionError:
        print("Please enter denominator other than zero  ")
    except TypeError as err:
        print("Please check the calculation :::  ", err)
    except OverflowError as err:
        print("Please enter value other than Zero :: ", err,
              " is not supported programmatically")
    except Exception:
        print(" error occurred ")

    else:
        z = x / y
        print("Z value :", z)
    finally:
        print("--end program---")


get_num(10, 20)

print(
    '-----------------------------------------------------------------------')

try:
    num = int(input("enter number:"))
except Exception as e:
    print("exception occurred")
else:
    print("num is ", num)
finally:
    print("end program")

try:
    list = [12, 3, 4, 6, 8, 9]
except Exception as e:
    print("exception occurred")
else:
    print("list :", list)
finally:
    print("end_program")




try:
    num = int(input("enter any number:"))
except Exception as e:
    print("exception occurred")
else:
    if num >= 0:
        if num == 0:
            print("zero")
        else:
            print("positive number")
    else:
        print("negative number")
finally:
    print("end_program")"""
"""in above program in try block there is  no exceptions else block and finally block executed ,
in exception occurred in try block except block will be executed"""

"""
def num():
    try:
        num = int(input("enter any number:"))
    except Exception:
        print("exception occurred")
    else:
        if num >= 0:
            if num == 0:
                print("zero")
            else:
                print("positive number")
        else:
            print("negative number")
    finally:
        print("end_program")


num()



try:
    n=int(input("Enter a number:"))
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
except Exception:
    print("exception occurred")
else:
    print("The total sum of digits is:",tot)

finally:
    print("end_program")  


try:
    num1 = int(input("enter num1 value:"))
    num2 = int(input("enter num2 value:"))
except Exception:
    print("exception occurred")
else:
    num3 = num1 + num2
    print("num3 value is ",num3)
finally:
    print("end program") 

num = int(input("enter number"))

if type(num) == str:
    print(num)

if type(num) == int:
    x = int(input("enter x"))
    y = int(input("enter y"))
    z = x + y
    print("addition of two numbers :", z)


else:
    print("end_program")

print(" username password with exception ")
try:
    username = input("enter your name")
    password = input("enter password ")

except Exception:
    print("exception occurred")

else:
    if username == "kumar" and password =="1234":
        print("successfully login")
finally:
    print("end program")


try:
    n = int(input("Enter the number to print the tables for:"))
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
except ValueError:
    print("please enter  number only")
except Exception as e:
    print("exception occurred", type(e))

else:
    print("program executed successfully")
finally:
    print("end_program")




try:
    with open('text1.txt','r') as f:
        f = f.readlines()
        f1 = str(f).split()
        print("****** normal text file ********")
        print("normal text file",f)
        print("****** after spilt the file ******")
        print("after split the file ",f1)
except Exception:
    print("exception occurred")
else:
    print("successfully read the file")
finally:
    print("end") """



try:
    dict1 = {'name': 'kumar', 'id': 27, 'loc': 'hyd'}
    print("normal dictionary  :", dict1)
    print("name :", dict1['name'])      # name : kumar
    print("id   :", dict1['id'])        # id : 27
    print("loc   :", dict1['loc'])
    print("company is :", dict1['company'])
except KeyError as ke:
    print("key is not found in dictionary")
else:
    print("name :", dict1['name'])
finally:
    print("end_program")