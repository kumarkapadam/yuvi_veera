"""__init__methos is similar to constuctor
constructors are used to initializing the object state
constructors are also conatins a collection of statements that are executed at the  time of object creation
it runs as soon as an object of a class is instantiated
"""

class student: # creating class
    def __init__(self,name,age):    #init method or constructor
        self.name = name            # name and age both are variables
        self.age =age               #self.name and self.age both are instance variables
    def stu_det(self):              # method
        print(f"student name is {self.name} and age is{self.age}")


#object instantiating
stu = student("veerendra",23)
stu.stu_det()