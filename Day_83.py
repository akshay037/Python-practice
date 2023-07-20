# Task number 90 :- Python Program to Compute the Power of a Number

base = input("Enter first number ")
exponent = input("Enter first number ")

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))