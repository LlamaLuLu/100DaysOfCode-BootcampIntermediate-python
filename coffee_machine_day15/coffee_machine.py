from resources import *

def show_menu():
    menu = {}
    print("\nOur Menu:")
    for i in MENU:
        menu[i] = MENU[i]['cost']
        print(i, " is $", menu[i], sep="")

# TODO: 1. print report
def report():
    water = f"Water: {assets['water']}ml"
    milk = f"Milk: {assets['milk']}ml"
    coffee = f"Coffee: {assets['coffee']}g"
    money = f"Money: ${assets['money']}"
    return f"{water}\n{milk}\n{coffee}\n{money}\n"


# TODO: 2. check resources sufficient
def check_res(drink):
    for i in drink['ingredients']:
        cost = drink['ingredients'][i]
        if assets[i] < cost:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


# TODO: 3. process coins
def coin_count():
    total = 0
    print("Please insert coins.")
    pennies = int(input("How many pennies? "))
    nickles = int(input("How many nickles? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))
    total += (quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
    return total


# TODO: 4. check transaction successful
def adjust_assets(drink):
    for i in drink['ingredients']:
        amount = drink['ingredients'][i]
        assets[i] -= amount


off = False
assets = resources
assets["money"] = 0

show_menu()
while not off:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino):\n")
    if user_choice == 'e' or user_choice == 'espresso':
        drink = MENU['espresso']
        drink_name = 'espresso'
    elif user_choice == 'l' or user_choice == 'latte':
        drink = MENU['latte']
        drink_name = 'latte'
    elif user_choice == 'c' or user_choice == 'cappuccino':
        drink = MENU['cappuccino']
        drink_name = 'cappuccino'
    elif user_choice == 'r' or user_choice == 'report':
        print(report())
        continue
    elif user_choice == 'off':
        print("Thank you for using the coffee machine!")
        off = True

    price = drink['cost']
    if check_res(drink):
        coins = coin_count()
        print(f"\nYou have entered: ${round(coins,2)}")
        if coins < price:
            print("Sorry that's not enough money. Money refunded...")
            continue
        else:
            assets['money'] += price
            change = coins - price
            if change > 0:
                print(f"Here is ${round(change,2)} in change.")
            adjust_assets(drink)
            print(f"Here is your {drink_name}. Enjoy!\n")
