# Task number 13 :- Python Program to Find the Largest Among Three Numbers

num1 = input("Enter first number ")
num2 = input("Enter second number ")
num3 = input("Enter third number ")

if num1 >= num2 and num1 >= num3:
    print("The largers number is ",num1)
elif num2 >= num3:
    print("The largers number is ",num2)
else :
    print("The largers number is ",num3)