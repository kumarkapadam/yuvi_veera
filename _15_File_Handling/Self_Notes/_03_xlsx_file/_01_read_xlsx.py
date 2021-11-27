"""

import openpyxl
wb = openpyxl.load_workbook("C:\\Users\\Kumar\\Desktop\\data.xlsx")
print(type(wb))

sheets = wb.sheetnames
print(sheets)

print(wb.active.title)
sh1 = wb['Sheet1']
print(type(sh1))


data = sh1['A1'].value
print(data)
data1 = sh1['A2'].value
print(data1)

# option1
print(wb['First Name']['B2'].value)

#option2
"""

x = 'kumar'
for i in x:
    print(i.upper())
print()


x = "kiran"
for i in range(len(x)):
    x[i].upper()
print(x)
