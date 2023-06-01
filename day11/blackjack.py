import random
import os
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, cpu_score):
    if user_score > 21 and cpu_score > 21:
        return "You went over. You lose."

    if user_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "You lose, Computer has blackjack"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "You went over, you lose."
    elif cpu_score > 21:
        return "Computer went over, you win!"
    elif user_score > cpu_score:
        return "You win!"
    else:
        return "You lose."


def play_game():
    print(logo)

    user_cards = []
    cpu_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            game_over = True
        else:
            get_new_card = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if get_new_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare(user_score, cpu_score))


while (
    input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y"
):
    os.system("clear")
    play_game()
