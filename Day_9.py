# Task number 11 :- Python Program to Check if a Number is Odd or Even

num = input("Enter a number ")

if int(num)%2 == 0:
    print("{0} is a Even number".format(num))
else:
    print("{0} is a Odd number".format(num))


# Task number 12 :- Python Program to Check Leap Year

year = int(input("Enter the year "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# 1988, 1992, 1996, and 2000