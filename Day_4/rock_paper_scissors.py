import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if player_choice >= 0 and player_choice <= 2:
    print(rps[player_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(rps[computer_choice])

message = ["You lose", "You win!", "It's a draw"]

if player_choice == 0:
    if computer_choice == 0:
        print(message[2])
    elif computer_choice == 1:
        print(message[0])
    else:
        print(message[1])
elif player_choice == 1:
    if computer_choice == 0:
        print(message[1])
    elif computer_choice == 1:
        print(message[2])
    else:
        print(message[0])
elif player_choice == 2:
    if computer_choice == 0:
        print(message[0])
    elif computer_choice == 1:
        print(message[1])
    else:
        print(message[2])
else:
    print("You entered an invalid number, so you lose.")
