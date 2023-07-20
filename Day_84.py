# Task number 91 :- Python Program to Count the Number of Digits Present In a Number

num = input("Enter first number ")
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))