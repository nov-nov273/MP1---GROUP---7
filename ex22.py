import math

s1 = float(input("Enter the length of Side 1: "))
s2 = float(input("Enter the length of Side 2: "))
s3 = float(input("Enter the length of Side 3: "))

sum = (s1 + s2 + s3)/2
area = sum * (sum - s1) * (sum - s2) * (sum - s3)

sr = math.sqrt(area)

print (f"The area of the triangle is:  {sr:.2f}")