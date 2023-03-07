dict = {}
while True :
    print("-----Birthday Reminder-----")
    print("1.Show Birthdays")
    print("2.Add to Birthday list")
    print("3.Exit")
    choice = int (input("Enter the choice "))
    if choice == 1 :
        if len (dict.keys()) == 0 :
            print("Nothing to show")
        else:
            name = input("Enter name to look for Birthday ")
            birthday = dict.get(name,"No data found")
            print(birthday)
    elif choice == 2 :
        name = input("Enter friends name ")
        data = input("Enter Birthday ")
        dict[name] = data
        print ("Birthday Added")
    elif choice == 3 :
        break
    else :
        print("Choose a valid option")