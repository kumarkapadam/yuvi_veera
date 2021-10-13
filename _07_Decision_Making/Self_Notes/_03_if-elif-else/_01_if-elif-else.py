#if elif else
#check number is positive  negitive  and zero
"""num = int(input("enter any number:"))
if num>0:
    print("positive number")
elif num == 0:
    print("---zero----")
else:
    print("negitive number") """

"""
num =int(input("enter any number"))
if num==10:
    print("matched with",num)
elif num==20:
    print("matched with",20)
else:
    print("not- matched")  """

# eligible for credit card
"""
salary = float(input("enter your salary"))
if salary >= 30000:
    print("eligible for credit card")
else:
    print("your not eligible for credit card")
    print("thank you")
"""
"""
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)

"""
"""
list=[]
num = int(input("enter number to be inserted"))
for i in range(num):
    n=int(input("enter number"))
    list.append(n)
print(list)
for i in range(len(list)):
    for k in list:
       if list[i]>k:
            a =list[i]
print(a)
"""

"""avg = int(input("enter marks"))
if avg>=90:
    print("A Grade")
elif avg >= 60:
    print("B Grade")
else:
    print("Fail") """
"""
telugu =int(input("enter telugu marks"))
hindi = int(input("enter hindi marks "))
english =int(input("enter english marks"))
maths =int(input("enter maths marks"))
science=int(input("enter science marks"))
num = 5
avg = (telugu + hindi + english + maths + science)//num
print(avg)

if avg >=90 and avg<=100:
    print('A Grade')
elif avg >=70 and avg <90:
    print("B Grade ")
elif avg >= 60 and avg>50:
    print("C Grade")
else:
    print("Fail")
"""

year = int(input("enter year"))

if (year % 4) == 0:
    if(year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
   print(year, "is not a leap year")





