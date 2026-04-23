import math
#User Input
Rad = float(input("Enter the radius of the circle: "))
#Calculations
Area = math.pi * Rad**2
Sphere_Volume = (4/3) * math.pi * Rad**3
#Output
print(f"The area of the circle is: {Area:.2f}")
print(f"The volume of the sphere is: {Sphere_Volume:.2f}")