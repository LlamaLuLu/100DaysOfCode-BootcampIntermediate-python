from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# TODO: 1. print report
# TODO: 2. check if resources sufficient?
# TODO: 3. process coins
# TODO: 4. check if successful transaction?
# TODO: 5. make coffee

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





