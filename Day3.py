# If-Else conditional statement
print("Welcome to ticket unit")
Name = input("What is your name? ")
Height = int(input("Enter your height: "))
bill = 0
if Height >= 120:
    print(f" {Name} Tell us your age to determine your ticket price")
    age = int(input("input your age: "))
    if age < 12:
        bill = 5
        print("Your Ticket price is $5!")
    elif age <= 18:
        bill = 8
        print(" Your Ticket price is $8!")
    else:
        bill = 12
        print("Your Ticket price is $12!")

    photo = input("Do you want a photo? ")
    if photo == "yes":
        bill += 3
        print(f"Your total bill is {bill}")
else:
    print(f"Your Height is {Height}, you are not eligible")


# Test for even and odd number
Number = int(input("Enter a number: "))
if Number % 2 == 0:
    print("It is an even number")
else:
    print("it is an odd number")

# Show if a particular year is a leap year or not
Year = int(input("Enter a year: "))
if Year % 4 == 0:
    print(f" Year {Year} is a leap year")
    if Year % 100 == 0:
        print(f" Year {Year} is a leap year")
        if Year % 400 == 0:
            print(f" Year {Year} is a leap year")
        else:
            print("Its not a leap year")
    else:
        print("its a leap year")
else:
    print("It is not a leap year")

