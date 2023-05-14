print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You\'re at a crossroad, where do you want to go? Type \"left\" or \"right\". ").lower()

if choice1 == "right":
    print("You turn to right and fall into a trap pit and die. Game Over.")
else:
    choice2 = input("You arrive to river, do you want to swim across the river or wait for someone to row past you and ask for help from them? Answer \"swim\" or \"wait\". ").lower()
    if choice2 == "swim":
        print("You start swimming across the river but the flow is too strong and you drown. Game Over.")
    else:
        print("You decided to wait. Luckily someone was rowing past you and helped you to the other side of the river.")
        choice3 = input("You find a house which has 3 doors: red, green and blue. Which door do you open? ").lower()
        if choice3 == "green":
            print("You opened the door and it led you to safe. You won!")
        else:
            print("You try to open the door but it was trapped with bomb which exploded. Game Over.")
