class Person:
    def __init__(self,name,age,loc):
        self.__name = name
        self._age  = age
        self.loc   = loc

    @property
    def name(self):
        return self.__name
    @name.setter
    def set_name(self,name):
        self.__name = name
    def per_det(self):
        print('name is :',self.__name)
        print('age is  :',self._age)
        print("location :",self.loc)



per = Person('naveen','20','hyd')
per.per_det()

per.set_name = 'kiran'
per.per_det()