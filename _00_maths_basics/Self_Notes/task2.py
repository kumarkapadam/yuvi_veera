# a list countain group of strings convert to capital


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

