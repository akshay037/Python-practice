# Task number 56 :- Python Program to Catch Multiple Exceptions in One Line

string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)