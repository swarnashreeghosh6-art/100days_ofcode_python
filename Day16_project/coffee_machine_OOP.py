from art import logo
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
print(logo)
menu=Menu()
coffee_machine=CoffeeMaker()
money_machine=MoneyMachine()
on=True
while on:
    choice = input(f"What would you like to have?{menu.get_items()}."
                   f"If you want to check the amount of resources left type \"report\": ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)







