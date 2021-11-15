class A:  # parent class
    def add(self):  # instance method
        a = 10
        b = 20
        c = a + b
        print("addition,", c)


class B(A):  # B is child class from A  , parent class from C
    def sub(self):  # instance method
        a = 20
        b = 2
        c = a - b
        print("subtraction :", c)


class C(B):  # child class
    def mul(self):  # instance method
        a = 12
        b = 3
        c = a * b
        print("mulplication a and b", c)

# object creation
ob = C()
ob.mul()
ob.sub()
ob.add()


class Grand_Father:
    def grand_det(self):  # instance method
        print("this is a grand father class")


class Father(Grand_Father):
    def father_det(self):  # instance method
        print("this is a father class")


class Son(Father):
    def son_det(self):  # instance method
        print("this is a son class")


# object creation
s = Son()
s.son_det()
s.grand_det()
s.father_det()

print(
    "-------------------multilevel inheritence------------------------------")


class Family:
    def show_family(self):
        print("This is our family:")


# Father class inherited from Family
class Father(Family):
    fathername = ""

    def show_father(self):
        print(self.fathername)


# Mother class inherited from Family
class Mother(Family):
    mothername = ""

    def show_mother(self):
        print(self.mothername)


# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()  # Object of Son class
s1.fathername = ""
s1.mothername = ""
s1.show_family()
s1.show_parent()
