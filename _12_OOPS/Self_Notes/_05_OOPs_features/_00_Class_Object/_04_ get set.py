#get method
# set method

class student:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def set_stu(self,height):
        self.height=height

    def get_stu(self):
        return self.height
    def show(self):
        print(f"student name is {self.name}  age is {self.age} and height is {self.height}")

    def compare(self,stu2):
        if self.age==stu2.age:
              return True
        else:
             return False
stu1 = student("kumar",23)
stu1.set_stu(6.8)
stu1.show()

stu2 =student('yuvi',24)
stu2.set_stu(6.1)
stu2.show()


if stu1.compare(stu2):
    print("both are same")
else:
    print("different")