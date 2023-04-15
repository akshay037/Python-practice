# Task number 22 :- Python Program to Display Powers of 2 Using Anonymous Function

terms = int(input("How many terms "))

result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

# Extra work :- Python Program to Display Powers of Any Number Using Anonymous Function Upto Any Term

num = int(input("Enter the number "))
terms = int(input("Enter the How many terms "))

result = list(map(lambda x: num ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print(num," raised to power",i,"is",result[i])