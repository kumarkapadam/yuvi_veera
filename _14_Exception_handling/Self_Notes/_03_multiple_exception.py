"""
try:
    a = [1, 2, 3, 4, 5, 6, 7]
    print("Second element ", a[1])
    print("Fourth element ", a[3])
    print("Fourth element ", a[7])
except:
    print("An error occurred")



print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))  # ValueError("invalid literal for int() with base 10: 'rewrew'")
    y = int(input("Enter denominator value:"))
    li = [5, 12, 23, 32]
    print("List val:", li[2])  # IndexError("list index out of range")
    print("Division :", x / y)  # ZeroDivisionError("division by zero")
    print("Hello world")
    print("---------------------------------")
except Exception as obj:  # Exception obj = ValueError()
    print("** Error occured :  ==> ", obj)
print("----REMAINING CODE-------")  """


