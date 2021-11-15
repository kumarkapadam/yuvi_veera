'''
Instance variables
Instance methods
'''


def func1():
    print("Function body")


func1()


class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):   # instance method
        print("Employee information : ", self.eid, self.name, self.sal)


kumar = Employee(27, 'kumar', 15000) # object creation
kumar.get_edata()




class Mobile:
    def __init__(self, mob_name, ram, color):  # constructor
        self.name = mob_name       # self.name ,self.ram , self.color all are instance variables
        self.ram = ram             # mob_name ram and color all are local variables
        self.color = color

    def mob_det(self):  # mob_det is a instance method
        print(
            f'mobile name {self.name} ram is {self.ram} color is {self.color}')


mob = Mobile('lenovo', '4GB', 'blue')  # object creation
mob.mob_det()
