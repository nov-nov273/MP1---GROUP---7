# 30

pressure_kpa = float(input("Enter a pressure in kilopascals: "))

# Conversion factor: 1 kPa = 0.145038 psi
psi = pressure_kpa * 0.145038

# Conversion factor: 1 kPa = 7.50062 mmHg
mmhg = pressure_kpa * 7.50062

# Conversion factor: 1 kPa = 0.00986923 atm
atm = pressure_kpa * 0.00986923

print(f"Pressure in kilopascals: {pressure_kpa:.2f} kPa")
print(f"Pressure in pounds per square inch: {psi:.2f} psi")
print(f"Pressure in millimeters of mercury: {mmhg:.2f} mmHg")
print(f"Pressure in atmospheres: {atm:.4f} atm")