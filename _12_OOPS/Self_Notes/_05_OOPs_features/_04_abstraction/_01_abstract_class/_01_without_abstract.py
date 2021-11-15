'''
We should not write concrete method in super class
Each sub class requires noofsides() behavior impl. in unique way
'''


# Without Abstraction
class Polygon():

    def noofsides(self):
        print("Polygon sides ??????")


class Triangle(Polygon):  # Triangle is a Polygon
    # overriding
    def noofsides(self):
        print("I am Triangle with 3 sides")


class Quadrilateral(Polygon):  # Quadrilateral is a Polygon
    # overriding
    def noofsides(self):
        print("I am Quadrilateral with 4 sides")


class Pentagon(Polygon):
    # overriding
    def noofsides(self):
        print("I am Pentagon with 5 sides")


poly_obj = Polygon()
poly_obj.noofsides()

quad_obj = Quadrilateral()
quad_obj.noofsides()

pent_obj = Pentagon()
pent_obj.noofsides()

print("******************")

'''
We should not write concrete method in super class
Each sub class requires  behavior impl. in unique way
'''

print("----------calculation without using abstract method----------")
import math


class Cal(object):
    def calculate(self):
        print(" math  calculations ")

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
