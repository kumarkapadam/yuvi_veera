set1 = {1,2,3,4,5}
print(set1) #{1, 2, 3, 4, 5}

set2 ={3,2,5,7,9}
print(set2) #{2, 3, 5, 7, 9}

print(set1.union(set2)) #{1,2,3,4, 5, 7, 9}
print(set1.difference(set2)) #{1, 4}
print(set2.difference(set1)) #{9, 7}
print(set1.intersection(set2)) #{2, 3, 5}
print(set1.symmetric_difference(set2)) #{1, 2, 3, 4, 5, 7, 9}
print(set1.issubset(set2)) #False
