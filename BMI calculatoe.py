num_char = len(str(input("What is your name? ")))
print(num_char)

W = int(input("Enter your weight in Kg: "))
H = int(input("Enter your Height: "))
BMI = W / H**2
print(int((BMI)))
if BMI < 18.5:
    print("You are  underweight")
elif BMI < 25:
    print("You are normal weight")
elif BMI < 30:
    print("you are overweight")
elif BMI < 35:
    print("You are obese")
else:
    print("you are clinically obese")
