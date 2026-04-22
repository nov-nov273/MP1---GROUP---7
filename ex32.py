# 32

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Smallest Value
smallest = min(num1, num2, num3)

# Largest Value
largest = max(num1, num2, num3)

# Mid value
total = num1 + num2 + num3
middle = total - smallest - largest

print("Sorted integers:")
print(smallest, middle, largest)