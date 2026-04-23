#17
#mcAt

c = 4.186

mass = float(input("Enter the mass of water in grams: "))

initial_temp = float(input("Enter the initial temperature of the water in Celsius: "))
final_temp = float(input("Enter the final temperature of the water in Celsius: "))

q = mass * c * (final_temp - initial_temp)

cost = 8.9

kw_hr = q / 3600000

coffee_cost = kw_hr * cost #cents
final_cost = coffee_cost / 100 #dollars

print(f"the amount of heat to raise the temp is: {q}J")
print(f"the cost of heat to raise the temp is: {final_cost:.5f}$")