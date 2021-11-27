"""

import csv

data = []
with open("phone_dataset.csv", 'r') as csv_file:
    csv_read = csv.reader(csv_file)
    # print(csv_read)
    for line in csv_read:
        data.append([line[0],line[1],line[2]])
        if data[: :1] == "John" or data[: :1] == "Doe":
            print("match")
            break
        else:
            print("un match")
print(data)

for row in data:
    print(row)

"""

list = [['Doe', ' John', ' New York'],
        ['Doe', ' John', ' California'],
        ['John', ' Smith', ' 9179581191'],
        ['Bill', ' Gates', ' (917) 358-1291'],
        ['Doe', ' John', ' Florida']]
print(list)
for i in list:
    if i[0] == "Doe" or i[1] =='John':
        print('match')
        print()
    else:
        print("unmatch")


