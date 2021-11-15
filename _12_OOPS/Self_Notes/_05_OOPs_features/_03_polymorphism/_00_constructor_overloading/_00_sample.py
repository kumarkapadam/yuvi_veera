# constructor overloading
'''
Constructor overloading means more than one constructor in a class with the same
name but a different argument (parameter). Python does not support Constructor overloading;
it has no form of function.
'''


class Student:
    def __init__(self, name, age, clg_name='jntuh',course='python'):  # constructor overloading
        self.name = name
        self.age = age
        self.clg_name = clg_name
        self.course = course

    def display(self):
        print(
            f'student name is {self.name} , age is {self.age} , clg_name is {self.clg_name},course {self.course}')


stu = Student('kumar', 24, 'jntuh', 'python')
stu1 = Student('kumar', 24, 'SK', 'java')
stu2 = Student('kiran', 24, 'JNTUA')
stu.display()
stu1.display()
stu2.display()

print("----------------student details------------")


class student:
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


stu = student()
stu.set_id(27)
print("id is :", stu.get_id())

stu.set_name('kumar')
print("student name is:", stu.get_name())
