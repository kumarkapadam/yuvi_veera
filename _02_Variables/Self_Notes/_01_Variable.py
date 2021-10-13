#what is variable
""" python variable is a reserved memory location to store values
     in python every value is a datatype"""


"""
one value can be reffered multiple variables
multiple  variable cannot reffered multiple values
"""
# rules for creating variables
""" variable name must start with a letter or the underscore character.
variable name cannot start with a number.
variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
Variable names are case-sensitive (name, Name and NAME are three different variables).
The reserved words(keywords) cannot be used naming the variable."""

"""
# example
_name ="kumar"
print(_name)

#starts with letter
a=10
print("starts with letter",a)

#variable name cannot start with number
11="hai" 
print(11) #syntax error cannot assign to literal """

a=10
b=20
print(id(a)) #1964346862160
print(id(b)) #1964346862480

x=y=10
print(id(x)) #1595959175760
print(id(y)) #1595959175760
y=20
print(id(x)) #2582201133648
print(id(y)) #2582201133968
#integer
a=19
print(type(a))
print(a)


#float
a=9.5
print(type(a))
print(a)


#string
str = 'welcome '
print(str)
print(type(str))

#complex
com=complex(2,3)
print(type(com))
print(com)



