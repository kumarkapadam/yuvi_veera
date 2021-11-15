def maximum(a, b, c):
    if  a >= b and  a>=c:
        largest = a

    elif (b >= c):
        largest = b
    else:
        largest = c

    return largest


# Driven code
a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))
print("maximum number is :",maximum(a,b,c))