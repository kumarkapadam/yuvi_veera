#default parameters
"""
class student :
    def __init__(self):
        self.name='kumar'
        self.age =24
    def stu_det(self):
        return self.name ,self.age

stu1=student()
print(stu1.stu_det()) """


# with parameter

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def stu_det(self):
        print("----------student details is-----------")
        print(f"student name is {self.name} and age is {self.age}")
stu1 =student('kamal',24)
stu1.stu_det()