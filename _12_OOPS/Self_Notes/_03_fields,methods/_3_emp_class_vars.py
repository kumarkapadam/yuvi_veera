print("---------------------------Without class variables-------------------")


class Student:
    def __init__(self, name, roll, college):
        self.name = name
        self.roll = roll
        self.college = college

    def get_stu_det(self):
        print(
            f'student name :{self.name}\nroll is :{self.roll}\ncollege is :{self.college}')


stu1 = Student('kumar', 27, 'JNTUH')
stu1.get_stu_det()

print("---------------------------With class variables-------------------")


class Student:
    college = 'jntuh'  # class variable, this is sharable to all objects

    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    def get_stu_det(self):
        print('college name :', Student.college)
        print(
            f'student name :{self.name} roll number is :{self.roll} age is :{self.age}')


stu1 = Student('kumar', 27, 24)
stu1.get_stu_det()

Student.college = 'sk'
stu2 = Student('kiran', 26, 20)
stu1.get_stu_det()
Student.get_stu_det(stu1)
