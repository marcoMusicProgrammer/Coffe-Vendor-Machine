class MenuItem:
    def __init__(self,name,cost,water,milk,coffe):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water,
            "milk":milk,
            "coffe":coffe
        }

    def to_string(self):
        print(f"{self.name}\n{self.cost}\n{self.ingredients}")


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffe=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffe=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffe=24, cost=3),
        ]

    def get_items(self):
        for item in self.menu:
            options = item.name
            print(options)

    def find_drink(self,drink_ordered):
        for drink in self.menu:
            if drink.name == drink_ordered:
                return drink
        print("Invalid drink selection")
