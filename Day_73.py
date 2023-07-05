# Task number 79 :- Python Program to Get the File Name From the File Path

import os

# file name with extension
file_name = os.path.basename('D:\Python programming\A_Task.txt')

# file name without extension
print(os.path.splitext(file_name)[0])

