"""import pandas

import pandas as pd

df = pandas.read_csv('C:\\Users\\Kumar\\Desktop\phone_dataset1.csv')

print(df)
print(" ************ data ********* ")
for i in df:
    print(i)

data1 = []
phone_data = open("C:\\Users\\Kumar\\Desktop\phone_dataset1.csv", 'r')
for i in phone_data.readlines():
    s = i.split(",")
    data1.append(s)
print(data1)
s1 = str(data1)


print(s1
print(" ******************   phone_data *************************")
for i in data1:
    print(str(i))

import csv

phone_data = open("C:\\Users\\Kumar\\Desktop\phone_dataset1.csv", 'r')
read = csv.reader(phone_data)

data = {}
for i in read:
    for j in range(len(i)):
        i=i[j].strip(" ' ")
        x=i.split()
    print(x[0]) """

