num_char = len(str(input("What is your name? ")))
print(num_char)

W = int(input("Enter your weight: "))
H = int(input("Enter your Height: "))
BMI = W / H**2
print(int((BMI)))

#Tell how many days, weeks, months left, if one is to live up to 90yrs

current_age = int(input("How old are you now? "))
Estimated_age = 90
Yrs_left = Estimated_age - current_age
Months = Yrs_left * 12
Weeks = Months * Yrs_left
Days = Yrs_left * Weeks

print(f"You have {Days} days, {Weeks} weeks, and {Months} Months till 90yrs")
