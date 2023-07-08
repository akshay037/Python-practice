# Task number 83 :- Python Program to Get Line Count of a File

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("D:\Python programming\Day_76.py"))