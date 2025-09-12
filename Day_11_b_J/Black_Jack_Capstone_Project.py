import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if c_score == u_score:
        return " Draw ;)"
    elif c_score == 0:
        return "You Lost, Computer had upper hand!"
    elif u_score == 0:
        return "You Win!!!"
    elif u_score > 21:
        return "You went over. You Lose"
    elif c_score > 21:
        return "Computer Lose, You win!!!"
    elif u_score > c_score:
        return "You Win!!"
    else:
        return "You Loseeeee"

def play_game():
    print(art.logo)
    user_cards = []
    computer_card = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for i in range(2):
        user_cards.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            ask_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if ask_user == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    # if ask_user == "n":
    #     print(f"Computer's final card: {computer_card}, Computer's final score: {computer_score}")
    # else:
    print(f"Computer's final card: {computer_card[0]}, Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a Black Jack game? Type 'y' for yes or 'n'") == "y":
    print("\n" * 25)
    play_game()












    # next_round = True
    #
    # while next_round:
    #     again_ask = input("Do you wan to play Back Jack game then type 'Y' or 'N' for pass.")
