"""laptop ={'name':'lenovo','ram':4,'made in':'india','cost':450000

}
print(laptop)

for dict in laptop:
    print(dict)

for key,value enumerate(dict):
    print(key,value) """

"""dict = {}
print(dict)
print(type(dict)) """
laptop ={'name':'lenovo','ram':4,'made in':'india','cost':450000}
print(laptop)

#getting value
print(laptop['name'])
print(laptop['ram'])

print(laptop.get('name'))

#update value
laptop['name']='hp'
print(laptop)

#adding in dict
laptop['address']='hyderabad'
print(laptop)

#removing
laptop.pop('name')
print(laptop)

laptop ={'name':'lenovo','ram':4,'made in':'india','cost':450000}
print(laptop)


"""
mobiles ={'lenovo':10000, 'redme' :12000 ,'real_me':15000,'iphone':50000}
for keys,values in enumerate(mobiles,start=1):
    print(keys,values)
    print(mobiles.get('lenovo'))
"""