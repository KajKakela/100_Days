from art import logo
import random


def play_game(difficulty):
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    correct_number = random.randint(1, 100)

    game_over = False

    while game_over == False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == correct_number:
            print("Correct! You won")
            game_over = True
        elif attempts == 1:
            print("You guessed too many times! You lost!")
            game_over = True
        elif guess < correct_number:
            attempts -= 1
            print("Too low, guess again.")
        elif guess > correct_number:
            attempts -= 1
            print("Too high, guess again.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty != "easy" and difficulty != "hard":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

play_game(difficulty)
