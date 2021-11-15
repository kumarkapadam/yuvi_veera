# Dynamic polymorphism   ==> Method overriding
""" method overriding ::  ability to change the method implements in
 child class which is available from parent """

class Animal:  # super class

    def __init__(self):
        pass

    def sleeping(self):  # instance method
        print("Animal sleeping")


class Tiger(Animal):

    def __init__(self):
        pass

    def sleeping(self):  # Method overriding
        print("Tiger sleeping")


tiger = Tiger()
tiger.sleeping()


class Car:
    def __init__(self):
        pass

    def get_data(self):
        print("discription of car")


class Bmw(Car):
    def __init__(self):
        pass

    def get_data(self):  # instance method
        print('description of bmw car')


c = Car()  # object creation
c.get_data()

c1 = Bmw()  # object  creation
c1.get_data()

print("--------------------method overiding---------------------")


class Parent:

    # Constructor
    def __init__(self):
        pass

    # Parent's show method
    def show(self):
        print("this is a parent class")


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        pass

    # Child's show method
    def show(self):
        print("this is child class")


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


class Parent:
    def __init__(self, city):
        self.city = city


class Child(Parent):
    def __init__(self, name, age, city):
        super().__init__(city)
        self.name = name
        self.age = age

    def display(self):
        print(f'this is child class')
        print(f'name is {self.name} age is {self.age} and city is {self.city}')


ob1 = Child('yuvi', 23, 'banglore')
ob1.display()


class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


class Student(Person):
    def __init__(self, fname, lname, age, college):
        super().__init__(fname, lname, age)
        self.college = college

    def display(self):
        print(f'this is child class')
        print(f'name is {self.fname} {self.lname} age is {self.age} ')
        print(f'college name is:', self.college)


stu1 = Student('kumar', 'kapadam', 24, 'JNTUH')
stu1.display()



print("------------method overriding-----------")


class Audi:  # Super class
    def discription(self): #instance method
        print("this is the description function of class audi")


class Bmw():  # sub class
    def discription(self):  #instance method
        print("this is the description function of class bmw")


audi = Audi()   # object creation
bmw = Bmw()     # object creation
for car in (Audi, Bmw):
    car.discription(bmw)
