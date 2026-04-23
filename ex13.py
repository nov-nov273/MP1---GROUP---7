cents = int(input("Enter the number of cents: "))

toonies = cents // 200
cents = cents % 200

loonies = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents // 1
cents = cents % 1

print("Your total change in coins is:")

print(f"toonies: {toonies}")
print(f"loonies: {loonies}")
print(f"quarters: {quarters}")
print(f"dimes: {dimes}")
print(f"nickels: {nickels}")
print(f"pennies: {pennies}")

