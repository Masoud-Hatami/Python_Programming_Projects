# Love Calculator

print("Welcome to the Love Calculator!")
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")
# lower case function
combined_string = name_1 + name_2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos. ")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is{love_score}, you are alright together. ")
else:
    print(f" Your score is {love_score}")