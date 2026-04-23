#19

import math

vi = 0
#vf = ?
a = 9.8 #gravity = 9.8 m/s^2
d = float(input("Enter the distance the object falls in meters: "))

vf = math.sqrt(math.pow(vi, 2) + 2*a*d)

print (f"final velocity of the object is {vf:.4f} m/s")