"""
self represents the instance of the class. By using the “self” keyword
we can access the attributes and methods of the class in python
"""


class Employee:
    def __init__(self, eid, name, sal):
        print("Self address  ", self)
        self.eid = eid  # instance variables : self.id  self.name  self.sal
        self.name = name # local variables  : eid,name,sal
        self.sal = sal

    def get_emp_info(self): # instance method
        print("Employee details are : ", self.eid, self.name, self.sal)


emp = Employee(27, 'kumar', 10000)  # object creation
emp.get_emp_info()

print("--------------------student----------------------")


class Student:
    def __init__(self):
        self.name = "kumar"
        self.age = 24
        self.roll_num = 27

    def stu_det(self):
        print(
            f'student name {self.name} age is {self.age} and roll_num {self.roll_num}')


stu = Student()  # object creation
stu.stu_det()

print("------------------employee----------------")


class Employee:
    def __init__(self):  # construtor
        self.name = "kiran"
        self.age = 20
        self.sal = 20000

    def display(self):  # instance method
        print('employee name :', self.name)
        print("age is        :", self.age)
        print("salary is     :", self.sal)


# create an instance to Student class
emp = Employee()
emp.display()  # call the method using the instance
