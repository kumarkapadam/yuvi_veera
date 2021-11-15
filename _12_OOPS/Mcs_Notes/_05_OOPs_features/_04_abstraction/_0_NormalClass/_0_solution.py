'''
abstraction describes the implementation hiding
abstraction ---import features of oops
            ---implementation hiding
            ---abstract class and abstract method
ABC     ---
        predefined module
        must be inherited from this class to create abstract class

@abstractmethod : predefined module @ abstractmethod

abstract class :  can not create the object of abstract class atleast one abstract method



'''
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


class Animal(ABC):

    def __init__(self):
        print("In Animal object")

    @abstractmethod
    def eating(self):  # Generic behavior
        pass


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # method overriding  is mandatory here
    def eating(self):
        print("Cat is Eating")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")


cat = Cat()
cat.sleeping()
cat.eating()

# SCENARIOS
print("--------------------------")


class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # method overriding  is mandatory here
    def eating(self):
        print("DOG is Eating")

    # Specific behavior
    def barking(self):
        print("DOG is barking")


dog = Dog()
dog.barking()
dog.eating()

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

print("------------abstract class --------------------")

from abc import ABC, abstractmethod

"""
    Animal
                                eating()    #body
                                running()   #body
                                sleeping()  #dont give body  (required in unique way)

                  Cat          Dog       Tiger      Lion
                  sleeping() sleeping() sleeping() sleeping()   # Method overriding"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def eating(self):  # generic behaviour
        print("animal eating")

    def running(self):  # generic behaviour
        print("animal running")

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
cat.running()
cat.sleeping()

print('----object creation-------')
dog = Dog()
dog.eating()
dog.running()
dog.sleeping()

print('----object creation-------')
tiger = Tiger()
tiger.eating()
tiger.running()
tiger.sleeping()

print("----------calculation using abstract method----------")
import math
from abc import ABC, abstractmethod


class Cal(ABC):
    @abstractmethod
    def calculate(self):
        pass

    def value(self, x):
        self.x = x


class Square(Cal):
    def calculate(self):
        print("square of a number     :", self.x * self.x)


class Square_root(Cal):
    def calculate(self):
        print("square_root of a number :", math.sqrt(self.x))


class Cube(Cal):
    def calculate(self):
        print("cube of a number        :", self.x ** 3)


squ = Square()
squ.value(10)
squ.calculate()

cube = Cube()
cube.value(10)
cube.calculate()

sqr = Square_root()
sqr.value(100)
sqr.calculate()
