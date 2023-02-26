from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    user = input(f'What would you like? {menu.get_items()}\n')

    if user == 'report':
        coffee_maker.report()
        money.report()

    elif user == 'off':
        is_on = False

    elif menu.find_drink(user) is not None:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
