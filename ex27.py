# 27
h = float(input("Enter your height: "))
w = float(input("Enter your weight: "))
unit = input("Did you use (M)etric or (I)mperial units?: ").lower()

if unit == 'i':
    bmi = (w / (h * h)) * 703
    print(f"Your BMI is: {bmi:.2f}")
elif unit == 'm':
    bmi = w / (h * h)
    print(f"Your BMI is: {bmi:.2f}")
else:
    print("Invalid unit choice.")