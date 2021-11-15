class Student:
    # instance variables :self.name  self.roll self.course
    # local variables    :name,roll,course
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def stu_det(self):  # instance method
        print(
            f'student name {self.name} roll number is {self.roll} and course {self.course}')


#object creation
stu1 = Student('kumar', 20, 'python')
stu1.stu_det()
