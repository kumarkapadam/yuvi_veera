"""
1.Encapsulation in Python is the process of wrapping up variables and methods into a single entity.
 In programming, a class is an example that wraps all the variables and methods defined inside it.


2.Encapsulation can be achieved using Private and Protected Access Members.
3. Private variables are preceded by using two underscores.
       __name it is example of private variable
4. Protected variables are preceded by using a single underscore.
       _age ,it is example of protect variable


public variable ,and public methods accessable anywhere
private variable and private methods accesable only  in there own class


"""


class My_data:

    def __init__(self, a, b):  # instance variables : self.__a ,self._b
        self.__a = a  # local variables : a,b
        self._b = b

    def data(self):
        print("a value is ", self.__a)
        print("b value is ", self._b)

    def _add_data(self):  # instance method using protect
        print("addition of two numbers",
              self.__a + self._b)  # addition of two numbers 30


obj = My_data(20, 10)
obj.data()
obj._add_data()

print("----------------employee data using encapsulation-------------------")


class Employee:
    def __init__(self, name, id, age, designation):
        self.name = name
        self._id = id
        self.age = age
        self.__designation = designation

    def get_emp(self):
        print('employee name is   :', self.name)
        print('id is              :', self._id)
        print('age                :', self.age)
        print("designation        :", self.__designation)


emp1 = Employee('kumar', 27, '25', 'python_developer')
emp1.get_emp()

print("------change the employee id-------")
emp1._id = 28
emp1.get_emp()

print("---------------student --------------------")


class Student:
    def __init__(self, name, age, roll, loc):
        self.name = name
        self._age = age
        self.__roll = roll
        self.loc = loc

    def stu_data(self):  # instance method
        print('student name:', self.name)
        print('age is      :', self._age)  # _age is protect variable
        print("roll number :", self.__roll)  # __roll is a private variable
        print("location is :", self.loc)


print("------student details")

stu1 = Student('kumar', 24, 27, 'hyd')
stu1.stu_data()

stu2 = Student('yuvi', 20, 35, 'banglure')
stu2.stu_data()

stu3 = Student('kiran', 26, 27, 'chennai')
stu3.stu_data()

print("-------- call private variables out side the class---------")

class Person:
    def __init__(self,name,age,loc):
        self.__name = name
        self._age  = age
        self.loc   = loc

    @property
    def name(self):
        return self.__name
    @name.setter
    def set_name(self,name):
        self.__name = name
    def per_det(self):
        print('name is :',self.__name)
        print('age is  :',self._age)
        print("location :",self.loc)



per = Person('naveen','20','hyd')
per.per_det()

per.set_name = 'kiran'
per.per_det()