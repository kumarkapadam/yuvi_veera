'''

2.X                      3.X
------------------------------------
range     xrange        range
------------------------------------
Iterator  Generator     Generator

Speed of execution : Iterator   --> More memory
Memory efficiency  : Generator  --> Less speed
'''
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list1:
    #print(i)
   # print(i , end=" ")
   print(i)

value = list1.__iter__()
print(value)
item1 = value.__next__()
print(item1)

'''
class Num:
    def __init__(self,num):
        self.n = 1
        self.num = num
    def __iter__(self):
        return self.n
    def __next__(self):
        if self.n <= self.num:
            result = self.n
            self.n+=1
            return result
        else:
            raise StopIteration

num = Num(10)
print(num.__iter__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
