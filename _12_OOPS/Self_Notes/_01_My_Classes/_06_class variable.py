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
