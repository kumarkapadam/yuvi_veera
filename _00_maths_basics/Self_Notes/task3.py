string = "karnataka"

dup = []

for char in string:
    if string.count(char) > 1:
         if char not in dup:
             dup.append(char)
print(dup)
print("k is repeating",string.count('k'))
print("a is repeating",string.count('a'))