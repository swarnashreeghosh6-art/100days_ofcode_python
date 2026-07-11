from art import logo
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 200,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def deduction(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

def check_resources(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def money_calc(user_want,order_ingredients):
    print("Please insert only rupees 10,20,50 notes")
    note_10 = int(input("How many 10 rupee notes: "))
    note_20 = int(input("How many 20 rupee notes: "))
    note_50 = int(input("How many 50 rupee notes: "))
    money_paid = (note_10 * 10) + (note_20 * 20) + (note_50 * 50)
    if money_paid > MENU[user_want]["cost"]:
        deduction(order_ingredients)
        change = money_paid - MENU[user_want]["cost"]
        print(f"Here is your change: {change}")
        print(f"Here is your {user_want.title()}☕.Enjoy!🥰")
    elif money_paid < MENU[user_want]["cost"]:
        print("Oops that's not enough money😢.Money refunded.")
    else:
        deduction(order_ingredients)
        print(f"Here is your {user_want.title()}☕.Enjoy!🥰")


game_over=False
while not game_over:
    user_want = input("What would you like to have? Espresso/Latte/Cappuccino."
                      "If you want to check the resources left,type \"Report\" : ").lower()
    if user_want == "off":
        game_over=True
    elif user_want == "report":
        print(f"Water:{resources["water"]}\n"
              f"Milk:{resources["milk"]}\n"
              f"Coffee:{resources["coffee"]}")
    else:
        drink = MENU[user_want]
        if check_resources(drink["ingredients"]):
            print(f"Cost is {drink["cost"]}")
            money_calc(user_want,drink["ingredients"])









