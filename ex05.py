#5
smalldeposit = 0.10
largedeposit = 0.25

smallcontainers = int(input("Enter the number of 1 liter containers: "))
largecontainers = int(input("Enter the number of containers that are larger than 1 liter: "))

refund = (smallcontainers * smalldeposit) + (largecontainers * largedeposit)

print(f"the Total refund = ${refund:.2f}")