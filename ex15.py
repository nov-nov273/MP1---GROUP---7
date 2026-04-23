# 15
feet = 0
while feet <= 0:
    feet = float(input('Enter your number in feet: '))
    if feet <= 0:
        print("Please enter a positive number for the distance in feet.")

inch = float(feet) * 12
miles = float(feet) / 5280
yards = float(feet) / 3

print(f"Your height in inches is: {inch:.2f}")
print(f"Your height in miles is: {miles:.2f}")
print(f"Your height in yards is: {yards:.2f}")