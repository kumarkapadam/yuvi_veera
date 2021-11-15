"""
abstraction describes the implementation hiding
abstraction ---import features of oops
            ---implementation hiding
            ---abstract class and abstract method
ABC     ---
        predefined module
        must be inherited from this class to create abstract class

@abstractmethod : predefined module @ abstractmethod

abstract class :  can not create the object of abstract class atleast one abstract method



"""
'''
                           Animal
                             eating()
                  Cat    Dog   Tiger    Lion

Here eating() is required for all sub classes
But each animal want their own implementation

Method :  signature
          body

'''

from abc import ABC, abstractmethod


class Animal(ABC):  # abstract class

    def __init__(self):
        print("In Animal object")

    @abstractmethod
    def eating(self):  # Generic behavior
        pass


def sleeping():
    print("Cat is sleeping")


class Cat(Animal):

    def __init__(self):
        super().__init__()
        print("In CAT object")

    # method overriding  is mandatory here
    def eating(self):
        print("Cat is Eating")

    # Specific behavior


cat = Cat()
sleeping()
cat.eating()

# SCENARIOS
print("--------------------------")


def barking():
    print("DOG is barking")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("In DOG object")

    # method overriding  is mandatory here
    def eating(self):
        print("DOG is Eating")

    # Specific behavior


dog = Dog()
barking()
dog.eating()

from abc import ABC, abstractmethod


class Car(ABC):  # abstract class
    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):  # method overriding
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):  # method overriding
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):  # method overriding
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):  # method overriding
        print("The mileage is 27kmph ")


# object creation
t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

print("------------abstract class --------------------")

"""
    Animal
                                eating()    #body
                                running()   #body
                                sleeping()  #dont give body  (required in unique way)

                  Cat          Dog       Tiger      Lion
                  sleeping() sleeping() sleeping() sleeping()   # Method overriding"""

from abc import ABC, abstractmethod


def running():  # generic behaviour
    print("animal running")


class Animal(ABC):
    def eating(self):  # generic behaviour
        print("animal eating")

    @abstractmethod
    def sleeping(
            self):  # eating() is required for all sub classes,but they required in unique way
        pass


class Cat(Animal):
    def sleeping(self):  # method overriding
        print("cat is sleeping")


class Dog(Animal):
    def sleeping(self):
        print("cat is sleeping")


class Lion(Animal):
    def sleeping(self):  # method overriding
        print("cat is sleeping")


class Tiger(Animal):
    def sleeping(self):  # method overriding
        print("cat is sleeping")


# object creation
cat = Cat()
cat.eating()
running()
cat.sleeping()

print('----object creation-------')
dog = Dog()
dog.eating()
running()
dog.sleeping()

print('----object creation-------')
tiger = Tiger()
tiger.eating()
running()
tiger.sleeping()

print("----------calculation using abstract method----------")
import math
from abc import ABC, abstractmethod


class Cal(ABC):  # abstract class
    @abstractmethod
    def calculate(self):  # abstract method
        pass

    def value(self, x):
        self.x = x


class Square(Cal):
    def calculate(self):  # method overriding
        print("square of a number     :", self.x * self.x)


class Square_root(Cal):
    def calculate(self):  # method overriding
        print("square_root of a number :", math.sqrt(self.x))


class Cube(Cal):
    def calculate(self):  # method overriding
        print("cube of a number        :", self.x ** 3)


print("------object creation ---")
squ = Square()
squ.value(10)
squ.calculate()
print("------object creation ---")
cube = Cube()
cube.value(10)
cube.calculate()
print("------object creation ---")

sqr = Square_root()
sqr.value(100)
sqr.calculate()

from abc import abstractmethod


class System:
    def __init__(self, ram, config, cost, color):
        self.ram = ram
        self.config = config
        self.cost = cost
        self.color = color

    @abstractmethod
    def sys_data(self):
        pass


class Lenovo(System):
    def sys_data(self):
        print('ram is        :', self.ram)
        print('config is     :', self.config)
        print('cost is       :', self.cost)
        print("color is      :", self.color)


class Dell(System):
    def sys_data(self):
        print('ram is        :', self.ram)
        print('config is     :', self.config)
        print('cost is       :', self.cost)
        print("color is      :", self.color)


# object creation
lenovo = Lenovo('4GB', "i5", 30000, 'red')
lenovo.sys_data()

dell = ('4GB', "i5", 30000, 'red')
dell.sys_data()
