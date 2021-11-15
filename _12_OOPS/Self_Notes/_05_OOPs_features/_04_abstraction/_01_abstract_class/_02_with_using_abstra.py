print("----------calculation using abstract method----------")
import math
from abc import ABC, abstractmethod


class Cal(ABC):  # abstract class
    @abstractmethod
    def calculate(self):
        pass

    def value(self, x):  # concrete method
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


squ = Square()  # object creation
squ.value(10)
squ.calculate()

cube = Cube()  # object creation
cube.value(10)
cube.calculate()

sqr = Square_root()  # object creation
sqr.value(100)
sqr.calculate()

"""create  car abstract class  that contains an instance variable ,concrete method and abstract method """

print("------------------create car abstract class------------")
from abc import ABC, abstractmethod


class Car(ABC):  # abstract class
    def __init__(self, regno):
        self.regno = regno

    def opentank(self):  # concrete method
        print("fill the fuel into the tank ")
        print("registration number is   :", self.regno)

    @abstractmethod  # abstractmethod
    def steering(self):
        pass

    @abstractmethod  # abstract method
    def braking(self):
        pass


class Maruthi(Car):
    def steering(self):  # method overriding
        print("manual steering")
        print("drive the car")

    def braking(self):  # method overriding
        print("maruthi uses hydralic brakes")
        print("apply breaks and stop it")


class Bmw(Car):
    def steering(self):  # method overriding
        print("power steering")
        print("drive the car")

    def braking(self):  # method overriding
        print("bmw uses gas brakes")
        print("apply breaks and stop it")


# object creation
bmw = Bmw(1234)
bmw.opentank()
bmw.steering()
bmw.braking()

maruthi = Maruthi(7654)  # object creation
maruthi.opentank()
maruthi.steering()
maruthi.braking()
