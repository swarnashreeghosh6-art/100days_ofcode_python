letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Easy version
import random
# pypass=""
# print("Welcome to the PyPassword Generator!")
# no_letters = int(input("How many letters would you like in your password?\n"))
# no_symbols = int(input("How many symbols would you like?\n"))
# no_numbers = int(input("How many numbers would you like?\n"))
# for i in range(1,no_letters+1):
#     l=random.choice(letters)
#     pypass+=l
# for j in range(1,no_symbols+1):
#     s=random.choice(symbols)
#     pypass += s
# for k in range(1,no_numbers+1):
#     n=random.choice(numbers)
#     pypass+=n
# print(pypass)

#Hard version
pypass=[]
print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))
for i in range(1,no_letters+1):
    l=random.choice(letters)
    pypass.append(l)
for j in range(1,no_symbols+1):
    s=random.choice(symbols)
    pypass.append(s)
for k in range(1,no_numbers+1):
    n=random.choice(numbers)
    pypass.append(n)
random.shuffle(pypass)
password=""
for p in pypass:
    password+=p
print(f"Your password is: {password}")







