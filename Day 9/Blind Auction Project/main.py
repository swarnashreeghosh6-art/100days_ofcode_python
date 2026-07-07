from art import logo
print(logo)

dict={}
condition=True
while condition:
    name=input("What's ur name? ")
    bid=int(input("What's ur bid? $"))
    dict[name] = bid
    yes_no=input("Are there other users who want to bid? Type yes or no: ").lower()
    if yes_no=="yes":
        print("\n" * 100)
    else:
        condition=False
max=0
winner=""
for i in dict:
    if dict[i]>max:
        max=dict[i]
        winner=i
print(f"The winner is {winner} with bid of ${max}")





