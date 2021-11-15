# P01 Req: sum of the elements in a list


'''
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->    |  =   +=    |   for
'''
# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")


def prime(num):
    if num > 1:
        s = int(num / 2)
        for i in range(2, s + 1):
            if num % i == 0:
                return "not prime"
                break
        return "prime"


num = int(input("enter any number:"))
print(prime(num))
