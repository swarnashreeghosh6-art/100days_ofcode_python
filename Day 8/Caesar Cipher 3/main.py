alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

def caesar(direction,message,shift):
    list = []
    for i in message:
        list.append(i)

    for j in range(len(list)):
        item = list[j]
        if direction=="encode":
            if item not in alphabet:
                list[j] = item
            else:
                index = alphabet.index(item)
                new_index = (index + shift) % 26
                list[j] = alphabet[new_index]
        else:
            if item not in alphabet:
                list[j] = item
            else:
                index = alphabet.index(item)
                new_index = (index - shift) % 26
                list[j] = alphabet[new_index]

    result = ""
    for k in list:
        result += k
    if direction=="encode":
        print(f"Here is the encoded result: {result}")
    else:
        print(f"Here's the decoded result: {result}")

condition=True
while condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    choice=input("Type 'yes' if you want to go again.Otherwise, type 'no'.").lower()
    if choice == "no":
        condition=False
        print("Over")






