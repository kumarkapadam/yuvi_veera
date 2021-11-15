print(
    "------1.Normal Inheritance: - 1.1 - Reuse super class methods  AS IS-------")


class Animal:
    def eating(self):
        print("this is animal class ")


class Tiger(Animal):
    def eating(self):
        print("this is tiger class")


ani = Animal()
ani.eating()

ani = Tiger()
ani.eating()


def m1():
    print("this is method m1 in class A")


class A:

    def m2(self):
        print("this is m2 method in class A")

    def m3(self):
        print("this is m3 method in class A")


class B(A):
    def m3(self):
        print("this is m3 method in class B")

    def m4(self):
        print("this is m4 method in class B")


# object creation
b = B()
b.m3()  # B class override class A
b.m4()  # B class override class A

m1()

print("---------------------inheritance---------------------------")


class Father:  # super class
    def __init__(self, name, age):  # parameterize constructor
        self.name = name  # instance variables : self.name self.age
        self.age = age  # local variables    : name ,age

    def father_data(self):  # instance method
        print(f'father name is :', self.name)
        print(f'age is         :', self.age)


class Son(Father):  # sub class
    def __init__(self, name, age):  # parameter constructor
        self.name = name  # instance variables : self.name , self.age
        self.age = age  # local variables :name,age

    def son_data(self):  # instance method
        print(f'son name is    :', self.name)
        print(f'age is         :', self.age)


# object creation
son = Father('kullayappa', 45)
son.father_data()

son = Son('kumar', 25)  # object creation
son.son_data()
