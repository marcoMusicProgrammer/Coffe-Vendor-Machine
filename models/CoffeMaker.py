class CoffeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffe": 100
        }

    #TODO
    """Prints a report of all resources."""
    def get_report(self):
        for ingredients in self.resources:
            print(f"{ingredients}: {self.resources[ingredients]}")

    #TODO
    """Returns True when order can be made, False if ingredients are insufficient."""
    def check_resources(self,drink):
        for ingredient in drink.ingredients:
            if self.resources[ingredient] >= drink.ingredients[ingredient]:
                return True
            else:
                print("Not enough resources")
                return False

    #TODO
    """Deducts the required ingredients from the resources."""
    def make_coffe(self,order):
        for ingredients in order.ingredients:
            self.resources[ingredients] -= order.ingredients[ingredients]

        print(f"Here is your {order.name}. Enjoy!")

