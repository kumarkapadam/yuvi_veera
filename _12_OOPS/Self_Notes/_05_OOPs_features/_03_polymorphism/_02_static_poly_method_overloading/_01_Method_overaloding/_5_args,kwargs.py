print("--------------------------*args-----------------------------")
def add(x, y, z):
    print("sum:", x + y + z)


add(10, 12, 13)

"""def add(x, y, z):
    print("sum:", x + y + z)


add(5, 10, 15, 20, 25)
# Typeerror add() takes 3 positional arguments but 5 were given"""


def add(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:", sum)


add(3, 5)
add(4, 5, 6, 7)
add(1, 2, 3, 5, 6)

print("------------------*args--------------------")


def get_data(*in_list):
    print(type(in_list), in_list)
    sum = 0
    for each in in_list:
        for val in each:
            sum += val
    print("Final sum : ", sum)


get_data([1, 2, 3, 4, 5], [1, 2, 4, 6, 5], (4, 3, 2, 2))

print("-------display all items------------")


def display(*list):
    for val in list:
        print(" display values is :", val)


display([1, 10, 11, 14, 15, 17], (1, 2, 3), {'kumar', 'yuvi', 'kiran'})

print("-----------using *args ---------------")


def add(*sum):
    tot = 0
    for i in sum:
        tot += i
    print("sum is:", tot)


add(1, 2, 3, 4, 6, 78)
add(10, 11, 12, 14, 15, 16, 20, 300)

print("------multiply using  *args-----------")


def multiply(*args):
    mul = 1
    for i in args:
        mul *= i
    print("multiplication of all values  :", mul)


multiply(1, 2, 3, 4, 5)


def list_mul(*multi):
    mul = 1
    for num in multi:
        for j in num:
            mul *= j
    print("multiplication of all values in list :", mul)


list_mul([1, 2, 3, 4, 5], [1, 2, 3])
list_mul([10, 11, 12, 13, 14])

print("---------multiplication using *args-----------")


def list_mul(*multi):
    mul = 1
    for num in multi:
        for j in num:
            mul *= j
    print("multiplication of all values in list :", mul)


list_mul([1, 2, 3, 4, 5], [1, 2, 3])
list_mul([10, 11, 12, 13, 14])
