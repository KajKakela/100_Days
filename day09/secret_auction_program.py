import os

all_bidders = {}

def login():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    all_bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    while other_bidders != "yes" and other_bidders != "no":
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if other_bidders == "yes":
        os.system("clear")
        login()
    else:
        highest_bidder = max(all_bidders, key=lambda k: all_bidders[k])
        highest_bid = all_bidders[highest_bidder]

        os.system("clear")
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

login()