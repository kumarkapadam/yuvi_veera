import json
from urllib.request import urlopen

with urlopen("https://www.gov.uk/bank-holidays.json") as response:
    source = response.read()
data = json.loads(source)

print(json.dumps(data , indent=2))

for key,value in data.items():
    print(key,"====",value)
for i in data['england-and-wales']['division']:
    print(i ,end="")

print("******************* data *******************")

comp_date = []
for i in data['england-and-wales']['events']:
    #print(i['title'],"=====",i['date'])
    date = i['date']
    print(date)
    comp_date.append(date)
print(comp_date)
date1 = str(comp_date)
years = []
for i in range(2016,2023):
    print(i)
    print(f"the holidays in {str(i)} in {date1.count(str(i))}")
