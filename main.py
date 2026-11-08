from coffee_machine import CoffeeMachine



def coffee_machine():
    cofee_vending_machine = CoffeeMachine()

    is_on = True

    while is_on:
        cofee_vending_machine.display_menu()
        code_drink = cofee_vending_machine.get_user_drink()
        try:
            if cofee_vending_machine.enough_resources(code_drink):
                if cofee_vending_machine.coin_operator(code_drink):
                    cofee_vending_machine.update_ingredients(code_drink)
        except KeyError:
            is_on = False


if __name__ == "__main__":
    coffee_machine()
