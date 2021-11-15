print("--------------operator overloading---------------------")

print("---integers------")
a = 10
b = 20
print("addition of two numbers:", a + b)  # (a.__add__(b))

print("-----strings-----")

str1 = 'hello'
str2 = 'kumar'

print("addition of two strings:", str1 + str2)  # (str1.__add__(str2))

print('----float------')

x = 10.03
y = 2.02
print("addition of two float:", x + y)  # (x.__add__(y))

print("---------------operator overloading ------------------------")
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_result(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, another_circle):
        return Circle(self.radius + another_circle.radius)

    def __sub__(self, another_circle):
        return Circle(self.radius - another_circle.radius)

    def __mul__(self, another_circle):
        return Circle(self.radius * another_circle.radius)

    def __gt__(self, another_circle):
        return Circle(self.radius > another_circle.radius)

    def __lt__(self, another_circle):
        return Circle(self.radius < another_circle.radius)

    def __ge__(self, another_circle):
        return Circle(self.radius >= another_circle.radius)

    def __le__(self, another_circle):
        return Circle(self.radius <= another_circle.radius)

    def __eq__(self, another_circle):
        return Circle(self.radius == another_circle.radius)

    def __ne__(self, another_circle):
        return Circle(self.radius != another_circle.radius)


c1 = Circle(10)
print(c1.get_result())
print(c1.area())

c2 = Circle(15)
print(c2.get_result())
print(c1.area())

c3 = c1 + c2
print(c3.get_result())

c3 = c2 - c1
print(c3.get_result())

c4 = c1 * c2
print(c4.get_result())

c5 = c1 < c2
print(c5.get_result())

c5 = c2 < c1
print(c5.get_result())

print("-----------Magic_Methods-------")

x = 10
y = 20
print("adding of two numbers               :", x.__add__(y))
print("subtraction of two numbers          :", x.__sub__(y))
print("multiplication of two numbers       :", x.__mul__(y))
print("greater than equal  of two numbers  :", x.__ge__(y))
print("less than or equal                  :", x.__le__(y))
print("greater than(compare two values)    :", x.__gt__(y))
print("less than(compare two values)       :", x.__lt__(y))
