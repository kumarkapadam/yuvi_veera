# class is a blueprint for an object or design
"""
class creates a user defined data structure,which holds its own data members and member function
which can be accessed and used by creating an instance of the class

classes are created by keyword of class
attributes are the variables that belongs to class
"""
# for example am taking a class as a student
"""
class student:
    pass

stu1=student()
print(type(stu1))
print(stu1)

stu2 =student()
print(type(stu2))
print(stu2) """


# class and instances
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student('hari', 25)
stu2 = Student('harith', 24)
print("--------student1 details-------------")
print(stu1.name)
print(stu1.age)

print("----------student2 details------------")
print(stu2.name)
print(stu2.age)
