# Task number 84 :- Python Program to Find All File with .txt Extension Present Inside a Directory

import glob, os

os.chdir("D:\Python programming\Read-and-write")

for file in glob.glob("*.txt"):
    print(file)