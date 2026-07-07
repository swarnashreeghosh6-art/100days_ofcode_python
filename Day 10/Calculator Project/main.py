from art import logo


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(logo)
    condition = True
    n1 = int(input("Enter the first number: "))
    while condition:
        operator = input("+\n-\n*\n/\nPick an operator: ")
        n2 = int(input("Enter the second number: "))
        result = operations[operator](n1, n2)
        print(f"{n1}{operator}{n2}={result}")
        choice=input(f"If you want to continue with {result},type 'y', or type 'n': ")
        if choice == "y":
            n1 = result
        else:
            condition=False
            print("\n"*20)
            calculator()

calculator()

















