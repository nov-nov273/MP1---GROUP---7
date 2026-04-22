# 09

principal = 0
while principal <= 0:
    principal = float(input("Enter the amount deposited: "))
    if principal <= 0:
        print("Please enter a positive number for the amount deposited.")

rate = 0.04
year1 = principal * (1 + rate) ** 1
year2 = principal * (1 + rate) ** 2
year3 = principal * (1 + rate) ** 3

print(f"After 1 year: {year1:.2f}")
print(f"After 2 years: {year2:.2f}")
print(f"After 3 years: {year3:.2f}")