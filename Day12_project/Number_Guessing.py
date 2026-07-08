import art_1
#COMPARISON
def compare(com_num,guess,game_over):
    i = 0
    guess_left=guess
    while i < guess and not game_over:
        num = int(input("Guess a number : "))
        if num == com_num:
            print("Correct😍")
            game_over = True
        elif num < com_num:
            print("Too low")
            guess_left-=1
            if guess_left == 0:
                print("Oops you have lost!😢")
            else:
                print(f"You have {guess_left} guesses left")
            i += 1
        else:
            print("Too high")
            guess_left-=1
            if guess_left == 0:
                print("Oops you have lost!😢")
            else:
                print(f"You have {guess_left} guesses left")
            i += 1
def play_again():
    again = input("Do you wanna play again? Type 'yes' or 'no' : ").lower()
    if again == "yes":
        print("\n" * 30)
        game()

def game():
    print(art_1.logo)
    import random
    com_num = random.randint(1, 100)
    print("WELCOME TO THE NUMBER GUESSING GAME!!\n"
          "I am thinking of a number between 1-100")
    e_h = input("Choose a difficulty. Type 'easy' or 'hard : ").upper()
    game_over=False
    if e_h == "EASY":
        guess=10
        print("You have 10 attempts to guess.")
        compare(com_num,guess,game_over)
    else:
        guess = 5
        print("You have 5 attempts to guess.")
        compare(com_num, guess,game_over)
    if game_over == False:
        print(f"Correct number was {com_num}")
    play_again()

game()





