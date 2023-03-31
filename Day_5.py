# Task number 7 :- Python Program to Generate a Random Number

from random import *

x = randint(1, 100)
print(x)

# Extra work :- Python Program to Generate a Random orders of number

from random import *

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(items)
print(items)

# Extra work :- Python Program to Generate a Random name with diffrent item numbers

from random import *

items = ['Tony','Aditya','Elroy','Manas','Piyush','Viraj']

x = sample(items,  1)   # Pick a random item from the list
print(x[0])

y = sample(items, 4)    # Pick 4 random items from the list
print(y)