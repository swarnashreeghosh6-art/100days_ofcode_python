cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import art
import random
#checking commit

def shuffle():
    card= random.choice(cards)
    return card
def calculate_score(cards):
    score=sum(cards)
    if score==21 and len(cards)==2:
        score=0
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return score

def blackjack():
    print(art.logo)
    def play_again():
        y_n_1 = input("Do you want to play a game of Blackjack? Type 'y' for yes, 'n' for no : ").lower()
        if y_n_1 == "y":
            print("\n" * 20)
            blackjack()
    #shuffling
    player_cards = []
    com_cards = []
    for i in range(2):
        player_cards.append(shuffle())
        com_cards.append(shuffle())
    score_player=calculate_score(player_cards)
    print(f"Your cards = {player_cards}, Current score = {score_player}")
    score_com = calculate_score(com_cards)
    print(f"Computer first card = {com_cards[0]}")

    if score_player==0 and score_com==0:
        print(f"Your final cards = {player_cards},  Final score = {score_player}")
        print(f"Computer's final cards = {com_cards},  Computer's final score = {score_com}")
        print("DRAW🙃")
    elif score_player==0:
        print(f"Your final cards = {player_cards},  Final score = {score_player}")
        print(f"Computer's final cards = {com_cards},  Computer's final score = {score_com}")
        print("You win with a blackjack!🥳")
    elif score_com == 0:
        print(f"Your final cards = {player_cards},  Final score = {score_player}")
        print(f"Computer's final cards = {com_cards},  Computer's final score = {score_com}")
        print("You lose!Dealer has blackjack!😢")
    else:
        condition = True
        while score_player < 21 and condition:
            y_n = input("Type 'y' to get another card,type 'n' to pass: ").lower()
            if y_n == "y":
                player_cards.append(shuffle())
                score_player=calculate_score(player_cards)
                print(f"Your cards = {player_cards},  Current score = {score_player}")
                print(f"Computer's first card = {com_cards[0]}")
            else:
                condition = False

            score_player=calculate_score(player_cards)
        print(f"Your final cards = {player_cards},  Final score = {score_player}")

        while score_com<17:
            com_cards.append(shuffle())
            score_com = calculate_score(com_cards)
        if score_com >21 and 11 in com_cards:
            com_cards.remove(11)
            com_cards.append(1)
            score_com=calculate_score(com_cards)
        print(f"Computer's final cards = {com_cards},  Computer's final score = {score_com}")
        if score_player > 21:
            print("BUST!YOU WENT OVER😢")
        elif score_com > 21:
            print("YOU WIN!🥳")
        elif score_player==score_com:
            print("DRAW🙃")
        elif score_com == 21 or score_player < score_com:
            print("YOU LOSE!😢")
        else:
            print("YOU WIN!🥳")
    play_again()

blackjack()





