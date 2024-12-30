from models.Menu import *
from models.CoffeMaker import *
from models.MoneyMachine import *

menu = Menu()
coffe_maker = CoffeMaker()
money_machine = MoneyMachine()

def main():

    quit = False
    while not quit:
        user_input = input("What would you like? (espresso/latte/cappuccino) ")

        match user_input:
            case "espresso"|"latte"|"cappuccino":
                cafe_machine_program(user_input)
            case "report":
                coffe_maker.get_report()
            case "quit":
                quit = True
            case _:
                print("Invalid command")


def cafe_machine_program(user_input):

    drink = menu.find_drink(user_input)
    check_resources = coffe_maker.check_resources(drink)

    if check_resources:
        check_money = money_machine.check_money(drink.cost)
        if check_money:
            coffe_maker.make_coffe(drink)
    else:
        main()


main()