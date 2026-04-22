# 31

num = input("Enter a number: ")

digits = list(num)

total = 0
expression = ""
for i in range(len(digits)):
    digit = int(digits[i])
    total = total + digit
    expression = expression + digits[i]
    if i != len(digits) - 1:
        expression = expression + " + "

print(f"{expression} = {total}")