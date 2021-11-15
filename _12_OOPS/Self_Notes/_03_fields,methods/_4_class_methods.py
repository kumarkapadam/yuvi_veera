'''
class Class:

    # STATE
        # ==> Fields(1,2)  which represents data

        1. Class variables
        2. Instance variables

    # BEHAVIOR
        # ==> Methods which represents implementation

       1. Class Method
       2. Instance Method
       3. Static method
'''


# Get employee count at a given point of time.


class Employee:
    comp = 'ORACLE'  # sharing
    emp_count = 0  # sharing + Modifying

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # instance method(can access instance,class variables)
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal,
              Employee.emp_count)

    # class method (can access only class variables)
    @classmethod
    def get_ecount(cls):
        print("Employee count : ", cls.comp, " -- ", cls.emp_count)


Employee.get_ecount()
madhu = Employee(100, 'Madhu N', 10000)
madhu.get_edata()  # instance method ==> Employee.get_edata(madhu)
Employee.get_ecount()  # class method    ==> Employee.get_ecount(Employee)
# To call class method, we can call using object,But don't do it.
madhu.get_ecount()

jaya = Employee(101, 'Jayadeep  Chowdary A', 20000)
jaya.get_edata()
Employee.get_ecount()

mohan = Employee(102, 'Mohan Kumar', 45000)
mohan.get_edata()
Employee.get_ecount()

'''
btech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)

        
employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY 
            
   

class variables    : data which is sharable to all objects
                     data which is SHARE + MODIFY actions
class methods      : 1. To act only on class variables


instance variables : data is unique for each object 
instance methods   : 1. To act only on instance variables OR 
                     2. Both instance and class variables
                     
                   

CV   - ClassMethod, InstanceMethod 
IV   - InstanceMethod
 
'''


class Employee:
    company_name = "modernize chip solutions pvt limited"

    def __init__(self, emp_name, emp_age):
        self.emp_name = emp_name
        self.emp_age = emp_age

    def emp_details(self):
        print("------------employee detials---------------")
        print(
            f"employee name {self.emp_name} and employee age is {self.emp_age}")


emp1 = Employee("kumar", 24)
emp1.emp_details()

print(emp1.company_name)
print(emp1.__dict__)

print(
    "-------------using class variable  instance varibale and  class method and instance method-------")


class Employee:
    raise_amount = 2.0
    number_of_employees = 0

    def __init__(self, first, last, age, salary):
        self.first = first
        self.last = last
        self.age = age
        self.salary = salary
        self.gmail = first + '-' + last + "@gmail.com"
        Employee.number_of_employees += 1

    def emp_full_name(self):
        print(f"employee full name is {self.first} {self.last}")

    def emp_details(self):
        print("-----employee details------------")
        print(
            f"employee name is {emp.emp_full_name()} self.age {self.age} salary is{self.salary}")

    def raise_salary(self):
        return self.salary * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp = Employee('kumar', 'kapadam', 24, 20000)
emp1 = Employee('kum', 'kk', 23, 15000)
emp.emp_details()
print(emp.salary)
print("---------after raising----------")
print(emp.raise_salary())
print(Employee.number_of_employees)

print(Employee.set_raise_amt(3))

print(emp.salary)
print("---------after raising----------")
print(emp.raise_salary())
print(Employee.number_of_employees)
