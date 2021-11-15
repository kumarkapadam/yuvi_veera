"""
interface :::  An abstract class will become an interface when it contains only
              abstract methods and there are no concrete methods
"""



"""from abc import ABC, abstractmethod


class System:
    @abstractmethod
    def sys_name(self):
        pass

    @abstractmethod
    def sys_data(self):
        pass


class Lenovo(System):

    def __init__(self, name, ram, config, color):
        self.sys_name = name
        self.ram = ram
        self.config = config
        self.color = color

    def sys_name(self):
        print("system name :", self.sys_name)

    def sys_data(self):
        print("ram is   :", self.ram)
        print("configure :", self.config)
        print("color     :", self.color)


def sym_name(self):
        self.sys_name = sys_name
        print('system name :', self.sys_name)

    def sys_data(self):
        self.ram = ram

# object creation
leno = Lenovo("len", "4GB", "i5", 'red')
leno.sys_name()
leno.sys_data()
"""

from abc import ABC, abstractmethod


class Car(ABC):  # abstract class

    @abstractmethod  # abstractmethod
    def steering(self):
        pass

    @abstractmethod  # abstract method
    def braking(self):
        pass


class Maruthi(Car):
    def __init__(self, regno):
        self.regno = regno

    def steering(self):  # method overriding
        print("register number :", self.regno)
        print("manual steering")
        print("drive the car")

    def braking(self):  # method overriding
        print("maruthi uses hydralic brakes")
        print("apply breaks and stop it")


class Bmw(Car):
    def __init__(self, regno):
        self.regno = regno

    def steering(self):  # method overriding
        print("Bmw registration number :",self.regno)
        print("power steering")
        print("drive the car")

    def braking(self):  # method overriding
        print("bmw uses gas brakes")
        print("apply breaks and stop it")


# object creation
bmw = Bmw(1234)
bmw.steering()
bmw.braking()

# object creation
print("------------object creation-----------")
maruthi = Maruthi(5432)
maruthi.steering()
maruthi.braking()

