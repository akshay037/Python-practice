# Task number 14 :- Python Program to Check Prime Number

num = int(input("Enter a number "))
i = 0

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
        #    print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

# Extra work :- Python Program to Check Prime Number between perticular range of numbers

lower_value = int(input ("Enter the Lowest Range Value: "))  
upper_value = int(input ("Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)