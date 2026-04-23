#14

cm = 2.54

feet, inches = input("Input height (feet'inches): "). split("'")
feet, inches = int(feet), int(inches)

height = (feet * 12 + inches) * 2.54

print (f"your height in cm is {height:.2f} cm")

