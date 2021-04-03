from abc import ABC
from ast import literal_eval
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious.")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is awesome.")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Put in tea bag, boil water, "
              f"pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Grind some beans, boil water, "
              f"pour {amount}ml, enjoy!")
        return Coffee()


def make_drink(kind):
    if kind == 'tea':
        return TeaFactory().prepare(200)
    elif kind == 'coffee':
        return CoffeeFactory().prepare(200)
    else:
        print(f"we don't have {kind} available with us.")


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialised = False

    def __init__(self):
        if not self.initialised:
            self.initialised = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available Drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories) - 1}): ')
        idx = int(s)
        s = input("Specify amount: ")
        amount = int(s)

        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    entry = input("What kind of drink would you like? ")
    drink = make_drink(entry)
    if drink:
        drink.consume()

    hdm = HotDrinkMachine()
    hdm.make_drink()
