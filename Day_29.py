# Task number 32 :- Python Program to Find Sum of Natural Numbers Using Recursion

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = int(input("Enter the number "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
