"""
write the program and fetch data using http get and point out number
of holidays in england & wales then group them based on year
"""
# import json
import json
from urllib.request import urlopen

url = "https://www.gov.uk/bank-holidays.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(type(data_json))
print(data_json)

for key, value in data_json.items():
    print(key, "------", value)
print(data_json['england-and-wales']['events'])

count = 0
date = []
temp_list = []
for i in data_json['england-and-wales']['events']:
    count = count + 1
    print(i['title'], "========", i['date'])
    date.extend([i['title'], i['date']])
    temp_list.append(i['date'])

print("num of holidays :", count)
print(date)
print(temp_list)
list_years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022','2023']
string1 = str(temp_list)
print(string1)
for year in list_years:
    print(f"the holiday in {year} is : {string1.count(year)}")






