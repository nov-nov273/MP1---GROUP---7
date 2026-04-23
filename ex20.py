R = 8.314

P = float(input("Enter pressure (Pa): "))
V = float(input("Enter volume (liters): "))
T = float(input("Enter temperature (Celsius): "))

V = V * 0.001
T = T + 273.15

n = (P * V) / (R * T)

print(n)