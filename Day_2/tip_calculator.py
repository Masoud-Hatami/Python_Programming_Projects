# Welcome message
print("Welcome to the tip calculator.")

# Get user input
bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

# Calculate tip and total bill
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount

# Calculate bill per person and round to 2 decimal places
bill_per_person = round(total_bill / people, 2)

# Print the final amount per person
print(f"Each person should pay ${bill_per_person}")


