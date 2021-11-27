"""Iterators are objects that can be iterated upon. In this tutorial,
you will learn how iterator works and how you can build your own iterator
using __iter__ and __next__ methods."""

'''
Step 1. On list object list1, __iter__() / iter() method will be called.
        list1.iter()  or list1.__iter__() 
        We will get iterator object    

Step2 : On iterator object, __next__() / next()  method will be called,
       so that we will get elements one by one in sequence.
'''

'''
Python Iterators :
Iterators are objects that can be iterated upon. 
Let us see how iterator works and how you can build your own iterator using __iter__ and __next__ methods.

1.What are iterators in Python?
==================================
  => Iterator in Python is simply an object that can be iterated upon. 
     An object which will return data, one element at a time.
  => Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators 
  etc. but hidden in plain sight.
  => Technically speaking, Python iterator object must implement two special methods, 
                  __iter__() and 
                  __next__(), 
                  collectively called the iterator protocol.
  => An object is called iterable if we can get an iterator from it. 
     Most of built-in containers in Python like: list, tuple, string etc. are iterables.
  => iter() function (which in turn calls the __iter__() method) returns an iterator from them.

2. Iterating Through an Iterator in Python
==========================================
  => We use the next() function to manually iterate through all the items of an iterator. 
     When we reach the end and there is no more data to be returned, it will raise StopIteration
'''

# in python everything is an object


list1 = []
print("type of list :", type(list1))
print("list1  is :", list1)

list2 = list()
print("type of list :", type(list2))
print("list1  is :", list2)

list3 = [1, 2, 3, 4, 5, 6]
"""for i in list3:
    print(i) """
value = list3.__iter__()
print(value)

item1 = value.__next__()
print(item1)
item2 = value.__next__()
print(item2)
item3 = value.__next__()
print(item3)
item4 = value.__next__()
print(item4)
item5 = value.__next__()
print(item5)
item6 = value.__next__()
print(item6)

"""item7 = value.__next__()
print(item7)  """  # StopIteration

print(" *********************     using for loop  ********************")
for i in list1:
    print(i)

my_list = [4, 7, 0, 3]  # 1. Define a list
my_iter = my_list.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
# print(my_iter.__next__())  # Exception occurs


try:
    list = [10, 20, 30, 40]
    value = list.__iter__()
    item1 = value.__next__()
    print(item1)
    item2 = value.__next__()
    print(item2)
    item3 = value.__next__()
    print(item3)
    item4 = value.__next__()
    print(item4)
    item5 = value.__next__()
    print(item5)
except StopIteration:
    print("out of the loop")
finally:
    print("******   end   ********")

print(" *********** using iter() and next() **********")

numbers = [11, 22, 33, 44, 55]
num = iter(numbers)
print(num)

num1 = next(num)
print(num1)
num2 = next(num)
print(num2)
num3 = next(num)
print(num3)
num4 = next(num)
print(num4)
num5 = next(num)
print(num5)
"""num6 = next(num)
print(num6)   # stopiteration

"""


class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self.n

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


even = Even(10)
print(next(even))
print(next(even))

print(" ***********   numbers ***********")


class Num:
    def __init__(self, num):
        self.n = 0
        self.num = num

    def __iter__(self):
        return self.num

    def __next__(self):
        if self.n <= self.num:
            self.n += 1
            return self.n
        else:
            raise StopIteration


num = Num(20)
print(next(num))
print(next(num))
print(next(num))
print(next(num))



print("***********   fibonacci  *********************")

class Fibo:
    def __init__(self,max,first=0,second=1):
        self.first = first
        self.second = second
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        next = self.first + self.second
        if next > self.max:
            return StopIteration()
        self.first = self.second
        self.second = next
        return next

fibo = Fibo(20)
iter = fibo.__iter__()
print(iter)

item = iter.__next__()
print(item)

item2 = iter.__next__()
print(item2)

item = iter.__next__()
print(item)

item2 = iter.__next__()
print(item2)






