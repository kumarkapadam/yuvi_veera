# read json file
import json

jsonfile = open(
    "H:\MCS-0027_MCS_Kumar_Corepython\_15_File_Handling\Self_Notes\jsonfile.json",
    'r')
jsondata = jsonfile.read()
print(jsondata)
jsonfile.close()
print(type(jsonfile))

# parse

obj = json.loads(jsondata)
print(str(obj["eBooks"]))
print(str(obj["eBooks"][0]))
print(str(obj["eBooks"][1]))
print(str(obj["eBooks"][2]))

print(str(obj["eBooks"][0]['language']))

print(str(obj["eBooks"][0]['edition']))

# convert
print("*****************  changing the data  **********************")
data = obj['eBooks']
print(data[0]['language'])

data[0]['language'] = 'python 3.0'
print(data)
print(type(data))

jsonfile.close()

import pickle

file3 = open("file3.txt", 'wb')
x = {
    'name': 'kumar',
    'id': 27
}
pickle.dump(x, file3)

file3.close()

file3 = open("file3.txt", 'rb')
y = pickle.load(file3)
print(y)
