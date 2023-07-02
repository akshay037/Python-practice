# Task number 79 :- Python Program to Trim Whitespace From a String

# using strip
my_string = " Python "

print(my_string.strip())

# using expression
import re

my_string  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)