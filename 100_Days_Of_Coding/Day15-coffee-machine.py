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
}

money = 0


# TODO : print report

def report():
    print('The resources report:')
    for i in resources:
        print(f"{i.capitalize()}: {resources[i]}")
    print(f"Money: ${round(money, 2)}")

# TODO : check resources sufficient

def check_resource(coffee_type):
    results = True
    lack_res = []
    for i in MENU[coffee_type]['ingredients']:
        if resources[i] < MENU[coffee_type]['ingredients'][i]:
            lack_res.append(i)
            results = False
    if len(lack_res) > 0:
        lack_str = ', '.join(lack_res)
        print(f"Sorry, there is not enough {lack_str}.")
    return results


# TODO : process coins

def coin_count():
    print('Please insert coins...')
    penny = int(input("How many penny: "))
    nickel = int(input("How many nickel: "))
    dime = int(input("How many dime: "))
    quarter = int(input("How many quarter: "))
    total = 0.01*penny + 0.05*nickel + 0.1*dime + 0.25*quarter
    return total

# TODO : check whether transaction is successful

def transaction(coffee_type):
    global money
    trans_status = True
    total_coin = coin_count()
    if total_coin < MENU[coffee_type]['cost']:
        print(f"The total coins inserted valued = {total_coin}.")
        print(f"The cost = {MENU[coffee_type]['cost']}.")
        print("Sorry that's not enough money. Money refunded.")
        trans_status = False
    elif total_coin > MENU[coffee_type]['cost']:
        print(f"The total coins inserted valued = {total_coin}.")
        print(f"The cost = {MENU[coffee_type]['cost']}.")
        print(f"The extra {round(total_coin - MENU[coffee_type]['cost'], 2)} is returned.")
        print("Please wait for awhile...the coffe is in process...")
        money += MENU[coffee_type]['cost']
    else:
        print("Please wait for awhile...the coffe is in process...")
        money += MENU[coffee_type]['cost']

    return trans_status

# TODO : Prompt user by asking “ What would you like? (espresso/latte/cappuccino)"
# TODO : turn off the machine by entering "off"
# TODO : if all criteria met, make coffee

def coffee():
    decision = True
    while decision:
        user = input('What would you like? (espresso/latte/cappuccino)\n')

        if user == 'report':
            report()
        elif user == 'off':
            print('Machine is OFF now...')
            break
        elif user in ['espresso', 'latte', 'cappuccino']:
            res = check_resource(user)
            trans = transaction(user)
            if res is True and trans is True:
                for k in MENU[user]['ingredients']:
                    resources[k] -= MENU[user]['ingredients'][k]

                print(f"Here is your {user}. Enjoy!\n")
        user_cont = input("Would you like for another oder? [y/n] ")
        if user_cont == 'n':
            decision = False

# initiate program
coffee()
