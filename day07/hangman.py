import random
from hangman_art import stages
from hangman_wordlist import word_list


chosen_word = random.choice(word_list)
lives = 6
display = []
guessed_letters = []


for letter in chosen_word:
    display.append("_")


while "_" in display:   
    guess = input("\nGuess a letter!: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess in guessed_letters:
        print(f"You already guessed letter {guess}!")
    elif guess not in chosen_word:
        lives -= 1
        print(stages[lives])
    
    guessed_letters.append(guess)

    print(*display)

    if "_" not in display:
        print("You won!")
    elif lives == 0:
        print("You lose!")
        print(f"The correct word was {chosen_word.upper()}.")
        break