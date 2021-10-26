''''''
'''
# Types 
1. Builtin/ Predefined    : print() id() type()   int float str list tuple dict set
2. User defined Functions : Programmer defined functions 
'''
# a = 100
'''
a  <==> variable 
100 <==> value
=  <==> Assignment operator 
'''
# print("Value of x : ", a)
'''
Function definition syntax :    def <func_name> () :    # f(var)
                                  # def sum(n1, n2):    # f(x)   

n1,n2 are parameters not variables


# function signature
def stu_det(name,age,ph_no):
    print(f"student name is {name} age is {age} phone_number is {ph_no}")

# functon calling
stu_det('kumar',25,9678)
stu_det("kiran",20,98765) 



def stu_grade(telugu,english,hindi,maths):
    res = telugu + english + hindi + maths
    print("the result is :",res)
    avg = res // 4
    print("average marks :",avg)
    if avg >0 and avg <100:
        if avg >90:
            print("A grade")
        elif avg>70:
            print("B grade")
        elif avg>50:
            print(" c Grade")
        else:
            print("Fail")

telugu = int(input("enter telugu marks:"))
english = int(input("enter english marks:"))
hindi = int(input("enter hindi marks:"))
maths = int(input("enter maths marks:"))

stu_grade(telugu,english,hindi,maths)  


print("-------------even numbers using function-----------------")
even = []
odd = []
def number(num):
    for i in range(1,num):
        if i%2==0:
            #print(i)
            even.append(i)
        else:
           # print(i)
            odd.append(i)

num = int(input("enter any number:"))
number(num)
print("even numbers",even)
print("odd numbers ",odd)      



def name(list):
    for i in list:
        if i == 'kumar':
            print("found")
            break
        else:
            print("not found")

list = ['kumar','kiran',10,20]
name(list)


print('------------------reverse number--------------')

def reverse(num):

    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    #print("Reverse of the number:", rev)
    return rev

num = int(input("enter any number:"))
reverse(num)
print("reverse of given number ",reverse(num))  '''


print("------------find the largest number in alist-------------------")

"""
def largest(list1):
    return list1[-1]

list = [10,20,13,4,11,16]
largest(list)
print("largest number in list:",largest(list))

def sorted(list):
    list1 = []
    num = int(input("how many numbers to be inserted:"))
    for i in range(num):
        elem = int(input("enter any number :"))
        list1.append(elem)
        list1.sort()
   # print("sorted list :",list1)
    return list1

sort = sorted(list)
print("sorted list :",sort)
"""






