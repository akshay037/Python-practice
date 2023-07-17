# Task number 88 :- Python Program to Check the File Size

import os

file_stat = os.stat('D:\Python programming\Day_80.py')
print(file_stat.st_size)