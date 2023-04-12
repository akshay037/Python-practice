# Task number 20 :- Python Program to Find Armstrong Number in an Interval

lower = int(input("Enter the number for lower limit "))
upper = int(input("Enter the number for upper limit "))

print("These are Armstrong Number")

for num in range(lower, upper + 1):

   order = len(str(num))
    
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:       
       print(num)