# A program that calculate BMI

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height)** 2
bmi_as_int = int(bmi)

print("Your BMI is : ", bmi)