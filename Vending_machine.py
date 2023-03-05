dict = {}
while True :
    print("-----ITEM LIST-----")
    print("1.Chocolate")
    print("2.Chips")
    print("3.Mints")
    print("4.Exit")

    Chocolate = 10
    Chips = 10
    Mints = 10

    choice = int (input("Enter the choice "))
    if choice == 1:
        order = input("Place order ")
        order = int(order)
        Chocolate - order
        print(Chocolate)
    elif choice == 2:
        order = input("Place order ")
        order = int(order)
        Chips - order
        print(Chocolate)
    elif choice == 3:
        order = input("Place order ")
        order = int(order)
        Mints - order
        print(Chocolate)
    elif choice == 4:
        break
    else:
        print("Choose a valid option")