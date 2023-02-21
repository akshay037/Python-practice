is_male = True
is_tall = False

if is_male:
    print("You are a male")


if is_male:
    print("You are a male")
else :
    print("You are not a male")


#for execution one condition should be true
if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You neither male or tall")


#for execution both condiction should be true
if is_male and is_tall:
    print("You are male or tall or both")
else:
    print("You are either not male or not tall or both")


#else if condition
if is_male and is_tall:
    print("You are male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not a male and not tall")