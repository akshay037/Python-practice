# Task number 96 :- Python Program to Count the Number of Occurrence of a Character in String

count = 0

my_string = input("Enter the string ")
my_char = input("Enter the string ")

for i in my_string:
    if i == my_char:
        count += 1

print(count)