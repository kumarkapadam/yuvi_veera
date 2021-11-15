
class Own_Exception(Exception):
    def __init__(self):
        print(" please enter other than zero")


def num():
    try:
        num = int(input("enter number:"))
        if num < 0:
            raise Own_Exception

    except Own_Exception as own:
        print(own)
    except ValueError:
        print("please enter positive number only")
    else:
        print("num is", num)
    finally:
        print("end_program")


num()



class AgeError(Exception):
    def __init__(self, message):
        self.message = message

try:
    age = int(input("Enter your age"))
    if age < 18:
        raise AgeError("**Not eligible**")  # manually raising exception as per our use case
    print("---You are eligible to vote-------")
    print("-----Voting process completed------")
except Exception as ageex:  # Exception ageex = AgeError("Not eligible")    # 5L Can <== 2L Water
    print("Exception :", ageex)
except AgeError as aer:
    print("AgeError :", aer)



class Num_Error:
    def __init__(self):
        print("enter integers only")



def add_numbers(x,y):
    try:
        x=int(input("enter x value"))
        y =int(input("enter y value"))
        sum = x + y
        print("sum is",sum)
    except Num_Error as err:
        print(err)

    else:
        print("sum is",sum)
    finally:
        print("end_program")
add_numbers(10,20)






