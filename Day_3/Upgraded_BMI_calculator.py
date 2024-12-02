# Upgraded BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your Weight in kg: "))
# round function round the number to the nearest whole number
bmi = round(weight / height ** 2)
print(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is{bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is{bmi}, You are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are obese.")
else:
    print(f"Your bmi is{bmi}, You are clinically obese.")

