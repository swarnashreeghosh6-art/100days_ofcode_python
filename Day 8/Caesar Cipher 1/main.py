alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(message):
    list = []
    for i in message:
        list.append(i)
    print(list)
    for j in list:
        index_1 = list.index(j)
        if j == " ":
            list[index_1] = " "
        else:
            index_2 = alphabet.index(j)
            list[index_1] = alphabet[index_2 + shift]
    print(list)
    result = ""
    for k in list:
        result += k

    print(f"Here's the encoded result: {result}!")
encrypt(text)


