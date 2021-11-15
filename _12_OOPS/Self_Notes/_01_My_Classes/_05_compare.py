class employee:

    def __init__(self,name,age,count=None):
        self.name = name
        self.age = age
        self.count=None

    def emp_det(self):
        print("------------employee details-------------")
        print(f"employee name is  {self.name} and age is {self.age}")


    def compare_age(self,emp2):
        if self.age == emp2.age:
            return True
        else:
            return False

emp1=employee('hari',23)
emp1.emp_det()

emp2=employee('yuvi',24)
emp2.emp_det()

if emp1.compare_age(emp2):
    print("both are same")
else:
    print("different")

