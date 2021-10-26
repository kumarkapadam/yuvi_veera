print("------------function calling-------------------")

a = int(input("enter a number:"))  # state # user input
b = int(input("enter b number:"))  # state # user input


def cal(a, b):  # function signature
    # function body
    print("addition of two numbers:", a + b)  # behaviour
    print("subtraction of two numbers:", a - b)  # behaviour
    print("multiplication of two numbers:", a * b)  # behaviour
    print("division  is", b / a)  # behaviour


# function calling
cal(a, b)




