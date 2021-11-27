"""import csv

with open("username.csv",'r') as csv_file:
    csv_read = csv.reader(csv_file)
    with open("username.txt",'w') as csv_file1:
         csv_write = csv.writer(csv_file1)
         for line in csv_read:
             csv_write.writerow(line)  """

import csv

with open("username.csv", 'r') as csv_file:
    csv_read = csv.DictReader(csv_file)
    with open("username.txt", 'w') as csv_file1:
        csv_write = csv.DictWriter(csv_file1 ,fieldnames= 'fields' ,delimiter = "\t")
        for line in csv_read:
            csv_write.writer(line)



