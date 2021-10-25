
str1 ="abc"
str2 ="defg"

for x,y in zip(str1,str2):
    print(x,y)
print(str2[-1])

"""



# a list countain group of strings convert to capital

"""
list =['kumar','kiran','raju']

name1=str(list).upper()
print("capital letter ",name1)


list = []
num  = int(input("enter how many strings inserted:"))
for i in range(num):
    name = input("enter any name")
    list.append(name)
print(list)
print("converted into the capital",str(list).upper())
str1 = str(list)



"""
#min and max

data = {'roll': 100, 'id': 1292, 'code': 88}

max = max(zip(data.values(), data.keys()))
print(max)
min = min(zip(data.values(), data.keys()))
print(min)
print(f'max value is {max} and min value is {min}') '''




print(
    "List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")


elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in (
"January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("Wrong month name")





string = "karnataka"

dup = []

for char in string:
    if string.count(char) > 1:
         if char not in dup:
             dup.append(char)
print(dup)  """