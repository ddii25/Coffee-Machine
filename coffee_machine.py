import json


class CoffeeMachine:
    """Simulates a coffee vending machine."""

    def __init__(self):
        self.ingredients = {
            "water": 500,
            "powdered milk": 250,
            "cocoa": 150,
            "coffee": 300,
            "powdered vanilla": 150,
        }
        self.total_coins = 0
        self.special_commands = ["on", "off", "report", "add"]

        with open("coffe.json", "r") as f:
            self.menu = json.load(f)

    def display_menu(self):
        """Show the user all the options our vending coffee machine offers."""
        num_item = 1
        for k in self.menu:
            print(f"{num_item}) {self.menu[k]['name'].upper()} {'% .2f' % self.menu[k]['cost']}€  ------  CODE: {k}")
            num_item += 1

    def get_user_drink(self):
        """Make sure the user picks a valid option."""
        is_on = True
        while is_on:
            user_order = input("> ").lower()
            if user_order in self.special_commands:
                if user_order == "add":
                    self.add_ingredient()
                elif user_order == "report":
                    self.report()
                elif user_order == "off":
                    self.get_coins()
                    print("Shut down the machine.")
                    return False
            try:
                for k in self.menu:
                    if k == user_order:
                        return user_order
                    else:
                        continue
            except ValueError:
                print("Executing a special command.")

    def coin_operator(self, code_drink):
        """Controls the coin operated system of the machine."""
        drink_price = self.menu[str(code_drink)]["cost"]
        coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
        total = 0
        for coin in coins:
            try:
                num = int(input(f"How many {'%.2f' % coin}€ > "))
            except ValueError:
                pass
            else:
                multiply = num * coin
                total += multiply
        if total >= drink_price:
            change = total - drink_price
            self.total_coins += drink_price
            print(f"Here's the change {round(change, 2)}€")
            return True
        elif total < drink_price:
            print(f"Not enough money\nCOST: {drink_price}€\nYOUR AMOUNT: {round(total, 2)}€")
            return False

    def enough_resources(self, code_drink):
        """Make sure the drink is able to make."""
        drink_ingredients = self.menu[code_drink]["ingredients"]
        values = []
        for ingredient in drink_ingredients:
            if ingredient in self.ingredients:
                if self.ingredients[ingredient] < drink_ingredients[ingredient]:
                    values.append(False)
                else:
                    values.append(True)
        if False in values:
            print(f"The machine doesn't have enough resources.\nSorry.")
            return False
        else:
            return True

    def update_ingredients(self, drink_code):
        """Once the operation is complete make the coffee"""
        drink_ingredients = self.menu[drink_code]["ingredients"]
        for ingredient in drink_ingredients:
            self.ingredients[ingredient] -= drink_ingredients[ingredient]

    def report(self):
        """Check the current status of th vending machine"""
        print(f"Total Coins: {self.total_coins}\n-----------------")
        print("Ingredients: \n----------------------------")
        for ingredient in self.ingredients:
            print(f"{ingredient.upper()}: {self.ingredients[ingredient]}")

    def add_ingredient(self):
        """Add more quantity of ingredients."""
        ingredients = [ingredient for ingredient in self.ingredients]
        update_ingredient = input("Which ingredient you want to access? ")
        if update_ingredient in ingredients:
            quantity_ingredient = float(input("Quantity: "))
            self.ingredients[update_ingredient] += quantity_ingredient

    def get_coins(self):
        """Take th money the machine made"""
        self.total_coins = 0
