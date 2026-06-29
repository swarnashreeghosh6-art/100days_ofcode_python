import random
import hangman_art
import hangman_words
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
lives=6

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in correct_letters:
        lives-=1
        print(f"You guessed {guess},that's not in the word."
          f"You lose a life.\n"
          f"****************************"
          f"{lives} LIVES LEFT****************************")
        print(hangman_art.stages[lives])

    if lives==0:
        game_over=True
        print(f"IT WAS {chosen_word}! YOU LOSE")

    if "_" not in display:
        game_over = True
        print(f"*************************YAYY YOU WIN!*************************")