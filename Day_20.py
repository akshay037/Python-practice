# Task number 24 :- Python Program to Convert Decimal to Binary, Octal and Hexadecimal

# Convert Decimal to Binary

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

dec = int(input("Enter the number "))

convertToBinary(dec)

# Python program to convert decimal into other number systems
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
