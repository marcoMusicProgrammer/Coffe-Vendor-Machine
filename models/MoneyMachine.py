from exceptions.ErrorMoney import ErrorMoney


class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarter":0.25,
        "dimes":0.10,
        "nickles":0.05,
        "pennies":0.01
    }

    def __init__(self):
       self.profit = 0
       self.money_received = 0

    #TODO
    """Prints the current profit"""
    def get_profit(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    #TODO
    """Returns the total calculated from coins inserted."""
    def get_total(self):
        right_input = False
        for value in self.COIN_VALUES:
            while not right_input:
                try:
                    num_coins = int(input(f"Insert {value}: "))
                    if num_coins < 0:
                        raise ErrorMoney("Number of coins must be positive")
                    self.money_received += num_coins  * self.COIN_VALUES[value]

                except ErrorMoney as e:
                    print(f"Error {e}")
                except ValueError:
                    print("You must insert an integer")

        return self.money_received

    #TODO
    """Returns True when payment is accepted, or False if insufficient."""
    def check_money(self,cost):
        self.get_total()
        if self.money_received >= cost:
            change = self.money_received - cost
            print(f"That's your change: {self.CURRENCY}{round(change,2)}")
            self.profit =+ cost
            self.money_received = 0
            return True
        else:
            print("Sorry but that's not enough money")
            self.money_received = 0
            return False