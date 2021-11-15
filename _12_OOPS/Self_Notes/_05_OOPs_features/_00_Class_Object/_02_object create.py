"""
object is an instance of a class

identity : it gives a unique name to an object and enables one object to interact with other objects
state :it is represent by the attributes of an object .it is also reflects the properties of AN OBJECT
behavior : it is represent by the methods of an object .it is also reflects the response of an object to the other objects
"""
'''

identity ---->student
here class is a student 
object is a collection of attributes and behaviour 
state--->attributes --> variables
behavior --> methods /functions '''


# creating class and objects

class Student:  # class
    def __init__(self):
        self.name = "kumar"
        self.age = 23

    def stu_name(self):  # method
        print("student name is", self.name)

    def stu_age(self):  # method
        print("student age is :", self.age)


# instantiation
stu = Student()

stu.stu_name()
stu.stu_age()
