# Task number 69 :- Python Program to Check If a String Is a Number (Float)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s12'))
print(isfloat('1.123'))