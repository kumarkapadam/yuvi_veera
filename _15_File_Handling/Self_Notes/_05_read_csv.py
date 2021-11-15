"""
import csv
with open("username.csv",'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    print(type(csv_reader))
    for line in csv_reader:
        print(line)
        print(line[0])
        print(line[1])
        print(line[2])
        print(line[3])


with open('new_names.csv','w') as new_file:
csv_writer = csv.writer(new_file , delimiter = '_')

for line in csv_reader:
   csv_writer.writerow(line)

"""
"""
import csv

with open("username.csv", 'r') as csv_file:
    csv_read = csv.reader(csv_file)
    print(csv_read)
    for line in csv_read:
        print(line)

with open("username1.csv", 'w') as csv_file_write:
    csv_write = csv.writer(csv_file_write, delimiter='_')

    for line in csv_write:
        csv_write.writerow(line)

import csv

with open("username.csv", 'r') as csv_file:
    csv_read = csv.reader(csv_file)
    with open("username1.csv", 'w') as csv_file_write:
        csv_write = csv.writer(csv_file_write, delimiter='_')

        for line in csv_read:
            csv_write.writerow(line)


"""
import csv
with open("username1.csv",'r') as csv_read:
     csv_file = csv.DictReader(csv_read)
     print(csv_file)
     for line in csv_file:
         print(line)