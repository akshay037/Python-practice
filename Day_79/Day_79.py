# Task number 85 :- Python Program to Get File Creation and Modification Date

import pathlib

# path of the given file
print(pathlib.Path("D:\Python programming\Day_79\Test.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())