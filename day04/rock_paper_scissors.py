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
images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
cpu_choice = random.randint(0,2)

if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(images[player_choice])
    print("\nComputer Chose:")
    print(images[cpu_choice])

    if player_choice > 2 or player_choice < 0:
        print("You typed an invalid number, you lose!")
    elif player_choice == 0 and cpu_choice == 2:
        print("You win!")
    elif cpu_choice == 0 and player_choice == 2:
        print("You lose!")
    elif cpu_choice > player_choice:
        print("You lose!")
    elif player_choice > cpu_choice:
        print("You win!")
    elif player_choice == cpu_choice:
        print("It's a draw!")