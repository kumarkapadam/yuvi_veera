tup = (1,2,4,[9,7,4,3],10,18,20)
print("tuple          :",tup)
print(tup[4])
# tup.append(10)    # AttributeError: 'tuple' object has no attribute 'append'
print(tup[3])
tup[3].append(15)
tup[3].append([15,10])
tup[3].append('yuvi')
tup[3].extend([10,98,'k'])
print(tup)
