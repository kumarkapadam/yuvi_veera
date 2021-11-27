import os
print(dir(os))
print(os.getcwd())
print(os.listdir())



import zipfile
my_zip = zipfile.ZipFile("files.zip",'w')
my_zip.write('test.txt')
my_zip.write('thumbnail.png')
my_zip.close()



import zipfile
my_zip = zipfile.ZipFile("files.zip",'w')
my_zip.write('test.txt')
my_zip.write('hello hai ')
my_zip.close()




