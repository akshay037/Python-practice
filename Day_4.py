# Task number 6 :- Python Program to Swap Two Variables

var1 = input("Enter first Variable ")
var2 = input("Enter Second Variable ")
Temp = 0

Temp = var1
var1 = var2
var2 = Temp

print("After change",var1)
print("After change",var2)

# Extra work :- Python Program to Swap Two Variables with using temp

var1 = input("Enter first Variable ")
var2 = input("Enter Second Variable ")

var2, var1 = var1, var2

print("After change",var1)
print("After change",var2)