import art
from game_data import data
import random

def compare(a,b):
    result=""
    if a>b:
        result="A"
    else:
        result="B"
    return result

done=[]
score=0
length=len(data)
game_over=False
condition=True


while not game_over:
    while condition:
        i = random.randint(0, length - 1)
        while i in done:
            i = random.randint(0, length - 1)
        done.append(i)
        j = random.randint(0, length - 1)
        while j in done:
            j = random.randint(0, length - 1)
        done.append(j)
        condition=False

    A=data[i]["follower_count"]
    B = data[j]["follower_count"]
    Compare=compare(A,B)
    print(art.logo)
    print(f"Compare A: {data[i]["name"]},{data[i]["description"]},from {data[i]["country"]}")
    print(art.vs)
    print(f"Compare B: {data[j]["name"]},{data[j]["description"]},from {data[j]["country"]}")
    A_or_B=input("Who has more followers? Type \"A\" or \"B\" : ").upper()
    if A_or_B==Compare:
        print("You are correct!")
        score+=1
        print(f"Your current score is {score}")
    else:
        print(f"Oops you are wrong!\nYour score is {score}")
        game_over=True
    i = j
    j = random.randint(0, length - 1)
    while j in done:
        j = random.randint(0, length - 1)
    done.append(j)
    if len(done)==len(data):
        print("Game over")
        game_over=True











