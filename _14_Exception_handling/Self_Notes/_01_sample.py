"""
try:
    list = []
    num = int(input("enter how many numbers to be inserted:"))
    for i in range(num):
        elem = int(input("enter number"))
        list.append(elem)
    print("list is ",list)
    print("index of list",list[5])

except IndexError as ve:
    print("index out of the range ")

except Exception as e:
    print("error occurred ",type(e))

finally:
    print("*******   end_program   *******")




try:
    age = int(input("enter your age"))
    if age > 18:
        print(" eligible for vote ")
    else:
        print('not eligible for vote')



finally:
    print("end program")



text_file = open("text1.txt",'w')
print(text_file.write("hellooo"))
text_file.close()


text_file = open("text1.txt",'a')
print(text_file.write("hellooo welcome to python programming"))
text_file.close()


text_file = open("text1.txt",'r')
print(text_file.read())
text_file.close()


try:
    age = int(input("enter your age"))
    if age > 18:
        print(" eligible for vote ")
    else:
        print('not eligible for vote')
except ValueError as ve:
    print("please enter integer number")
except Exception as e:
    print("exception occurred")

finally:
    print("end program")


try:
    file_open = open('text2.txt','w')
    print(file_open.write("hello kumar"))
    print("file open successfully")
    file_open.close()
finally:
    print("end ")
"""


