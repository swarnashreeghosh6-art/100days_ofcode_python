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
condition=True

while condition:
    i = random.randint(0, length - 1)
    while i in done:
        i = random.randint(0, length - 1)
    done.append(i)
    j = random.randint(0, length - 1)
    while j in done:
        j = random.randint(0, length - 1)
    done.append(j)
    A=data[i]["follower_count"]
    B = data[j]["follower_count"]
    Compare=compare(A,B)
    print(art.logo)
    print(f"Compare A: {data[i]["name"]},{data[i]["description"]},from {data[i]["country"]}")
    print(art.vs)
    print(f"Compare B: {data[j]["name"]},{data[j]["description"]},from {data[j]["country"]}")
    A_or_B=input("Who has more followers? Type \"A\" or \"B\" : ").upper()
    if A_or_B!=Compare:
        print(f"Oops you are wrong!\nYour score is {score}")
        condition=False
    score += 1
    if len(done)==len(data):
        print(f"Your score is {score}")
        print("Game over")
        condition=False
    print("\n" * 30)








