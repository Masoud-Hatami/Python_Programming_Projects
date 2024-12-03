import random

# Generate a random number between 0 and 1
random_number = random.randint(0, 1)

# Determine the outcome based on the random number
if random_number == 1:
    print("Heads")
else:
    print("Tails")