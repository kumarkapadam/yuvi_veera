
''''''
'''
# DATA TYPES
numbers  - individual values
boolean  - individual value
String   - group of values  'A'  '1'  '100'  '193.4'

# DATA STRUCTURES
String
List **
Tuple 
Dictionary **
Set

Collections module : NamedTuple OrderedDict DefaultDict FrozenSet Counter 
'''
# numbers
'''
int 
float
complex : 3i+4j
'''
# boolean
True
False


x = 10
print(x)   # f(x)
print("Value is :", x)

x = 10 + 20
# LHS = RHS


# Naming conventions
# variables always small letter

# REQ: Receive employee id and print it.

'''
Step 1: Receive employee id 
Step 2: Print it
'''
     # Hard coding the value :: Static way
e_id = 4325  # emp_id empid eid e_id   st_rno strno prod_id
print("Employee id : ", e_id)

     # Receive the value dynamically
e_id = input("Enter your employee id :")
print("Employee id : ", e_id)

'''
f(x) = 2x + 1  # Mathematics

Python function
def f(x):
    val = 2x + 1
    print(val)
'''

print("--------------------type--------------")
print("Type of 10 :", type(10))
eid = 100
print("Employee details : ", eid, type(eid))

eid = input("Enter employee id :")
print("Employee details : ", eid, type(eid))

eid = int(input("Enter employee id :"))
print("Employee details : ", eid, type(eid))

e_sal = float(input("Enter employee salary :"))
print("Employee details : ", e_sal, type(e_sal))

eid = 100
print("Employee id and it address : ", eid, id(eid))
msg = 'Hello World'
print("Message is : ", msg, type(msg), id(msg))

print("-----------------------------------student details-----------------------------------")
stu_name = input("enter student name")
print("student name is              :", stu_name)
print("name is which type           :",type(stu_name))
print("student address              :",id(stu_name))

stu_roll = int(input("enter student roll number"))
print("student roll number is        :",stu_roll)
print("which type student roll number:",type(stu_roll))




stu_address = input("enter student address:")
print("student address is                 :",stu_address)
print("student adress type is             :",type(stu_address))