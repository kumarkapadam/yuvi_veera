class Employee:
    def __init__(self, emp_name, emp_id, location, designation):
        # instance variables :self.emp.name  self.emp_id  self.location  self.designation
        # local variables    : emp_name,emp_id,location,designation
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.location = location
        self.designation = designation

    def emp_det(self):  # instance method
        print(
            f'employee name {self.emp_name}  id is {self.emp_id} location {self.location} {self.designation} developer')


# object creation
emp = Employee('kumar', 27, 'hyd', 'python')
emp.emp_det()
