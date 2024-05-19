# Task number 8 :- Python Program to Convert Kilometers to Miles

kilo_meter = input("Enter value of Kilometer ")
miles = 0.62137119

result = int(kilo_meter) * miles

print('%f is Total Miles'%result)

# Extra work :- Python Program to Convert Miles to Kilometers

kilo_meter = 1.609347
miles = input("Enter value of Miles ")

result = int(miles) * kilo_meter

print('%f is Total Miles'%result)

# Extra work :- Python Program to Convert diffrent length

def KM_to_miles(length,miles):
    miles = 0.62137119
    result = int(length) * miles
    return result
def miles_to_KM(length,KM):
    KM = 1.609347
    result = int(length) * KM
    return result
def default(length,KM):
    return "Incorrect day"

switcher = {
    1: KM_to_miles,
    2: miles_to_KM
    }

print('''You can perform operation
1. KM_to_miles
2. miles_to_KM
''')

def switch(operation):
    return switcher.get(operation, default)()

#Take input from user
choice = int(input("Select operation from 1,2: "))
length = int(input("Enter length number: "))

print (switch(choice))
