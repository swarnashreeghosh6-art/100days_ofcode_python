rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user=input("Choose:Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
R_P_S=[rock,paper,scissors]
computer=random.choice(R_P_S)
if user == "0":
    print(rock)
    print("Computer chooses:")
    print(computer)
    if computer == rock:
        print("Tie")
    elif computer == paper:
        print("You lose")
    else:
        print("You win")
elif user == "1":
    print(paper)
    print("Computer chooses:")
    print(computer)
    if computer == rock:
        print("You win")
    elif computer == paper:
        print("Tie")
    else:
        print("You lose")
else:
    print(scissors)
    print("Computer chooses:")
    print(computer)
    if computer == rock:
        print("You lose")
    elif computer == paper:
        print("You win")
    else:
        print("Tie")

