import math

#Earth's radius in kilometers
Earth_radius_km = 6371.01

#User Input
t1 = float(input("Enter the latitude of the first point in degrees: "))
g1 = float(input("Enter the longitude of the first point in degrees: "))
t2 = float(input("Enter the latitude of the second point in degrees: "))
g2 = float(input("Enter the longitude of the second point in degrees: "))

#Convert degrees to radians
t1_rad = math.radians(t1)
g1_rad = math.radians(g1)
t2_rad = math.radians(t2)
g2_rad = math.radians(g2)

#Calculate the distance using the formula
distance = Earth_radius_km * math.acos(math.sin(t1_rad) * math.sin(t2_rad) + math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))

#Output
print (f"\nThe distance between the two points is: {distance:.2f} kilometers.")