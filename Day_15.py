# Task number 19 :- Python Program to Check Armstrong Number

lengthnum = int(input("Enter the length of number: "))
num = int(input("Enter a number: "))
sum = 0


temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** lengthnum
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
