#----------------adding------------
tup1=(1,2,3,5,6)
tup2=(2,5,8,2,9)
print(tup1+tup2) #(1, 2, 3, 5, 6, 2, 5, 8, 2, 9)

#-----------------slicing------------
print(tup1[1:4]) #(2, 3, 5)
print(tup1[3:]) #(5, 6)


#--------------multiplying---------------------
tup3=tup1*2
print(tup3) #(1, 2, 3, 5, 6, 1, 2, 3, 5, 6)

#__________len-----------
print("length of the tuple1",len(tup1)) # length of the tuple1 5

print("-------------------------min-------------------------")
print("minimum value in tuple1",min(tup1)) #minimum value in tuple1 1

print("------------------------max-------------------------------")
print("maximum value in tuple1",max(tup1))# maximum value in tuple1 6
