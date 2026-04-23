import math

s = float(input("Enter side length: "))
n = float(input("Enter number of sides: "))

area = (n * s * s) / (4 * math.tan(math.pi / n))

print(area)