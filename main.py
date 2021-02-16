MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def check_sufficient_resources(drink):
    # Checks to make sure machine has sufficient resources to make the drink requested.

    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def process_coins():
    # Prompts user to input the number of each coin deposited and returns total dollar amount
    total = 0
    for coin, value in [('quarters', .25), ('dimes', .10), ('nickels', .05), ('pennies', .01)]:
        while True:
            try:
                total += int(input(f"how many {coin}? ")) * value
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
    return total


def perform_transaction(drink, money):
    # Checks to ensure the money deposited is enough to purchase the requested drink. If user deposited too much
    # change is calculated. The cost of the drink is then added to the machine's resources.

    cost = MENU[drink]['cost']
    if money >= cost:
        if money > cost:
            print('Here is ${:,.2f} dollars in change.'.format(money - cost))
        resources['money'] += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    # Removes the amount of each ingredient required to make the requested drink from the machine's resources.

    for ingredient in MENU[drink]['ingredients']:
        resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!")


# Turn the machine On
isOn = True

while isOn:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        # Turn Machine Off
        isOn = False
        continue
    if user_input == 'report':
        # Print machine report
        print(f"Water: {resources.get('water')}ml")
        print(f"Milk: {resources.get('milk')}ml")
        print(f"Coffee: {resources.get('coffee')}g")
        print("Money: ${:,.2f}".format(resources.get('money')))
        continue
    if user_input in ['espresso', 'latte', 'cappuccino']:
        # Attempt drink purchase
        if check_sufficient_resources(user_input):
            deposited = process_coins()
            if perform_transaction(user_input, deposited):
                make_coffee(user_input)
            else:
                continue
        else:
            continue
