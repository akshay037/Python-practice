# Task number 39 :- Python Program to Check Whether a String is Palindrome or Not

my_str = input("Enter the string ")

my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
