"""
there are two types files   1. text files
                            2.binary files


text file ::  text files store the data in the form of characters,
              text files are used to store characters or string.
==========

write : to write a data into file. if any data is already present in the file,
        it would be deleted and the present data  will be stored.

read  : to read  data from the file the file pointer is positioned at
        the beginning of the file
append : to append data to the file.append means adding the existing data
         the file pointer is place at the end of the file.
         if the file does not exist,it will create new file for writing data.
"""
"""

print("---------write a file-------------------")

file_write  =  open("file.txt",'w')
file_write.write("hello welcome to the python ,this is write file ")
file_write.close()


file_write = open("file.txt",'a')
file_write.write("\n high level programming language ")
file_write.close()


file_write = open("file.txt",'r')
print(file_write.read())
file_write.close()




# create a text file

file = open('file.txt','w')
str = input("enter any string")
file.write(str)
file.close()


# read text file
file  = open("file.txt",'r')
print(file.read())
file.close()


print("              ********************************************            ")

file1  = open("file1.txt",'w')
file1.write("1. Easy to code  2. Free and Open Source 3. Object-Oriented Language"
            "4. High-Level Language,5. Python is Portable language")
file1.close()


file1 = open("file1.txt",'r')
print(file1.read())
file1.close()


file1 = open("file1.txt",'r')
print(file1.readline())
file1.close()





file1 = open("file1.txt",'r')
print(file1.readlines())
file1.close()
"""

print(" *******************        read lines        **********")
file1 = open("file1.txt", 'r')
x = file1.readlines()
print(type(x))
x.append("6.simple")
print(x)
file1.close()

print(" ********************   read line ***************************")
file1 = open("file1.txt", 'r')
x = file1.readline()
print(type(x))
print(x)