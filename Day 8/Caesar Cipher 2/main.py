alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(direction,message,shift):
    def encrypt(message, shift):
        list = []
        for i in message:
            list.append(i)
        print(list)
        for j in range(len(list)):
            item=list[j]
            if item == " ":
                list[j] = " "
            else:
                index = alphabet.index(item)
                new_index = (index + shift) % 26
                list[j] = alphabet[new_index]
        print(list)
        result = ""
        for k in list:
            result += k
        print(f"Here's the encoded result: {result}!")

    def decrypt(message, shift):
        list = []
        for i in message:
            list.append(i)
        print(list)
        for j in range(len(list)):
            item = list[j]
            if item == " ":
                list[j] = " "
            else:
                index = alphabet.index(item)
                new_index = (index - shift) % 26
                if new_index<0:
                    new_index=-new_index
                list[j] = alphabet[new_index]
        print(list)
        result = ""
        for k in list:
            result += k
        print(f"Here's the decoded result: {result}!")
    if direction=="encode":
        encrypt(text,shift)
    else:
        decrypt(text,shift)
caesar(direction,text,shift)






