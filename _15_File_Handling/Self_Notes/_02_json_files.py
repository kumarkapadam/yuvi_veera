"""const_JSONData = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": 7,
    "key5": None,
    "favFriends": ["Kolade", "Nithya", "Dammy", "Jack"],
    "favPlayers": {"one": "Kante", "two": "Hazard", "three": "Didier"}
}

print(type(const_JSONData))
print(const_JSONData)

for key, value in const_JSONData.items():
    print(key, "-----", value)
print("key1 value is     :", const_JSONData['key1'])
print("key2 value is     :", const_JSONData['key2'])
print("key4 value is     :", const_JSONData['key4'])
print("favFriends value is     :", const_JSONData['favFriends'])
for friends in const_JSONData['favFriends']:
    print(friends)

# friends key ,value pairs


print("favplayers value is     :", const_JSONData['favPlayers'])
for players in const_JSONData['favPlayers']:
    print(players)
for key, value in const_JSONData['favPlayers'].items():
    print(key, "-----", value)
"""
import pandas
df = pandas.read_json("https://www.gov.uk/bank-holidays.json")
print(df)
df.to_csv("res.csv")
print(df)

df.to_excel("results.xlsx")
print(df)