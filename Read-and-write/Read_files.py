employee_file = open("D:\Python programming\Read-and-write\z-employees.txt", "r") # r stands for reading the file

#.readable makes files readable to user
print(employee_file.readable())


#.read the whole file    
#print(employee_file.read())


#.readline reads only first line
print(employee_file.readline())  


#.readlines reads the file in the form of list if you want to read perticular line pass the value in square bracket show as per line number 17 (just comment down the .read fucntion line)
#print(employee_file.readlines())
print(employee_file.readlines()[5])  


employee_file.close()