# You can order Pizza Now!

print("Welcome to Python Pizza Deliveries! ")
size = input("What pizza size do you want? S, M, or L \n ")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you whant Extra cheese?Y or N \n")

bill = 0
if size =='S':
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")









