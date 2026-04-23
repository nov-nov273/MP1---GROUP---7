# 28
temp = float(input("Enter the air temperature in Celsius: "))
wind = float(input("Enter the wind speed in km/h: "))

if temp > 10:
    print("Wind chill index is only valid for temperatures 10 degrees Celsius or below.")
elif wind <= 4.8:
    print("Wind chill index is only valid for wind speeds exceeding 4.8 km/h.")
else:

    wci = 13.12 + (0.6215 * temp) - (11.37 * (wind ** 0.16)) + (0.3965 * temp * (wind ** 0.16))

    wci_rounded = round(wci)
    print(f"The wind chill index is: {wci_rounded}")