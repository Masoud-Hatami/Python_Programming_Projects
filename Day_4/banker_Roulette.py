# Banker Roulette

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

# Get the total number of people
num_people = len(names)

# Generate a random index between 0 and the number of people - 1
random_choice = random.randint(0, num_people - 1)

# Select the person who will pay
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy the meal today.")