# 33

price_per_loaf = 3.49
discount_rate = 0.60
loaves = 0
while loaves <= 0:
    loaves = int(input("Enter the number of day old loaves being purchased: "))
    if loaves <= 0:
        print("Please enter a positive number.")

regular_price = loaves * price_per_loaf
discount = regular_price * discount_rate
total_price = regular_price - discount

print(f"Regular price:  ${regular_price:>7.2f}")
print(f"Discount:       ${discount:>7.2f}")
print(f"Total price:    ${total_price:>7.2f}")