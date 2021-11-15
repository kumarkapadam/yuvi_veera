class A:  # super class
    def a(self): # instance method
        print("this is class a")


class B: # super class
    def b(self):  # instance method
        print("this is class b")


class C(B, A):  # method resolution order left to right
    def c(self):  # instance method
        print("this is class c")


ob = C()  # object creation
ob.b()
ob.a()
ob.c()

print("----------------multiple inheritence--------------------")


# Father class created
class Father:
    fathername = ""

    def show_father(self):
        print(self.fathername)


# Mother class created
class Mother:
    mothername = ""

    def show_mother(self):
        print(self.mothername)


# Son class inherits Father and Mother classes
class Son(Father, Mother):  # M.R.O method resolution order
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()  # Object of Son class
s1.fathername = ""
s1.mothername = ""
s1.show_parent()

print("--------------multiple inheritence ---------------")


class Father:  # super class
    def father_det(self, name, age):
        self.name = name
        self.age = age
        print('father name is :', self.name)
        print('age is      :', self.age)


class Mother:  # super class
    def mother_det(self, name, age):
        self.name = name
        self.age = age
        print('father name is :', self.name)
        print('age is      :', self.age)


class Son(Father, Mother):  # M.R.O(method resolution order) # left to right
    def son_det(self):
        print('father name is :', self.name)
        print('age is         :', self.age)
        print('mother name is :', self.name)
        print('age is         :', self.age)


s = Son()
s.father_det('', 10)
s.mother_det('', 20)
s.son_det()
