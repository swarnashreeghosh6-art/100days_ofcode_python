cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import art
import random

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
def compare(score_player,score_com):
    if score_player == score_com:
        return "DRAW🙃"
    elif score_player == 0:
        return "You win with a blackjack!🥳"
    elif score_com == 0:
        return "You lose!Dealer has blackjack!😢"
    elif score_player > 21:
        return "BUST!YOU WENT OVER😢"
    elif score_com > 21:
        return "OPPONENT WENT OVER.YOU WIN!🥳"
    elif score_com == 21 or score_player < score_com:
        return "YOU LOSE!😢"
    else:
        return "YOU WIN!🥳"

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
    score_com = calculate_score(com_cards)

    game_over=False
    while not game_over:
        print(f"Your cards = {player_cards}, Current score = {score_player}")
        print(f"Computer first card = {com_cards[0]}")
        if score_player==0 or score_com==0 or score_player > 21:
            game_over=True
        else:
            y_n = input("Type 'y' to get another card,type 'n' to pass: ").lower()
            if y_n == "y":
                player_cards.append(shuffle())
                score_player = calculate_score(player_cards)
            else:
                game_over=True

    while score_com!=0 and score_com < 17:
        com_cards.append(shuffle())
        score_com = calculate_score(com_cards)
    print(f"Your final cards = {player_cards},  Final score = {score_player}")
    print(f"Computer's final cards = {com_cards},  Computer's final score = {score_com}")
    print(compare(score_player,score_com))

    play_again()

blackjack()





