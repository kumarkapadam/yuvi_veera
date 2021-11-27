# import json
import json
from urllib.request import urlopen
import csv

url = "https://www.gov.uk/bank-holidays.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(type(data_json))
# print(data_json)
"""
with open("sample.json", "w") as outfile:
    json.dump(data_json, outfile)
# now we will open a file for"""


with open('sample.json') as json_file:
    data = json.load(json_file)

# Write only the Pokemon name

file_csv = open('json_to_csv4.csv', 'w')

csv_writer = csv.writer(file_csv)

# Get the header
csv_writer.writerow(data.keys())
for i in data.keys():
    print(i)

for row in data:
    csv_writer.writerow(data.values())
    csv_writer.writerow(data['england-and-wales'])
    csv_writer.writerow(data['scotland'])
    csv_writer.writerow(data['northern-ireland'])




# csv_writer.writerow(data[''].values())


file_csv.close()
