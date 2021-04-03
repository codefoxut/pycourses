
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.rat_added = Event()
        self.rats = []

    def calculate_attack(self, rat):
        self.rat_added.append(rat)
        self.rats.append(rat)
        return len(self.rats)

    def reduce_attack(self, rat):
        self.rat_added.remove(rat)
        self.rats.remove(rat)


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        self.attack = self.game.calculate_attack(self)

    def __exit__(self, *args, **kwargs):
        self.game.reduce_attack(self)

    def __enter__(self):
        return self



if __name__ == '__main__':
    _game = Game()

    rat1 = Rat(_game)
    print(rat1.attack)

    rat2 = Rat(_game)
    print(rat1.attack, rat2.attack)

    with Rat(_game) as rat3:
        print(rat1.attack)
        print(rat2.attack)
        print(rat3.attack)

    print(rat1.attack, rat2.attack)
