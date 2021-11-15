'''
class structure
    # 1. Fields  - STATE
         class variables    - at class level,when state is shared among objects
         instance variables - at instance level, inside init method.
                              When each object required separate data


    # 2. Methods - BEHAVIOR
         class method       - cls parameter,which works only on class variables
         instance method    - self parameter,which works on only instance variables
                                                            both instance,class variables
                                                            only class variables XXX
        static method       - generic method

'''


class Employee:
    e_count = 0
    office = 'ORACLE'

    @classmethod
    def get_edata(cls):
        # print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)

    '''
    def __init__(self):
        pass
    '''


# no need to create object to call class methods
Employee.get_edata()  # Employee.get_edata(Employee)

# 2 way - Don't do it
obj = Employee()
print("Object address : ", obj)
obj.get_edata()  # ==> Employee.get_edata(obj)

print("------All methods---------")


class Employee:
    e_count = 0
    office = 'ORACLE'

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.e_count += 1

    @classmethod
    def get_edata(cls):
        # print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)

    def get_empinfo(self):
        print("Employee details : ", self.eid, self.name, self.sal)
        Employee.get_edata()
        # self.get_edata()


# to call class method
Employee.get_edata()
# to call instance method
madhu = Employee(101, 'Madhu Nettem', 15000)
madhu.get_empinfo()
madhu.get_edata()
Employee.get_edata()

print("-----static method--------")


# i want a behavior which neither deals with class variables nor instance variables

class Employee:
    @staticmethod
    def getinfo():
        print("Static method implementation")


Employee.getinfo()

'''
class Employee:
    1. STATE
    ----------
    # class variables   ==> during class loading
    # instance variables ==> init method
    
    2. BEHAVIOR
    -------------
    # class method      : works only on class variables 
    # instance method   : works only on instance variables 
                          works on both instance,class variables 
    # static method     : neither on class nor on instance variables 
'''


class Car:
    base_price = 10000  # class variable

    def __init__(self, windows, doors, power):  # constructor with parameters
        self.windows = windows  # local variables : windows,doors,power
        self.doors = doors  # instance variable : self.windows ,self.doors , self.power
        self.power = power

    def display(self):   # instance method
        print("--------car details---------")
        print(f"{self.windows} {self.doors} {self.power}")

    @classmethod
    def increment(cls, incre):  # class method
        cls.base_price = cls.base_price + cls.base_price * incre


car1 = Car(4, 6, 2000)  # object creation
car1.display()
print(car1.base_price)
car1.increment(10)
print(car1.base_price)
