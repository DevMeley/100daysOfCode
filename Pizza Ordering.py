print("Welcome to Dominos Pizza")
price = 0
Type = (input("Do you want an ordinary pizza? "))
if Type == "No":
    Pizza_Size = input("What size would you like? S, M, or L")
    if Pizza_Size == "S":
        price += 15
        print("Small size is $15!")
    elif Pizza_Size == "M":
        price += 20
        print("Medium size is $20")
    else:
        price += 25
        print("Large size is $25")
    Add_pepperoni = input("Do you want pepperoni? Y or n")
    if Add_pepperoni == "Y":
        if Pizza_Size == "S":
            price += 2
            print(price)
        else:
            price += 3
        print(price)
    else:
        print("none")
    Extra_cheese = input("do you want an extra cheese? y or n")
    if Extra_cheese == "y":
        price += 1
        print(price)
    else:
        print("non")
    print("Okay")
else:
    print("Here is your pizza!")
