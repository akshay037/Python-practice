# Task number 68 :- Python Program to Print Output Without a Newline

with open('D:\Python programming\Day_61\data_file.txt') as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)