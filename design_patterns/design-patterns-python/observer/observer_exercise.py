
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.rat_added = Event()
        self.rat_dies = Event()
        self.notify_rat = Event()


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        game.rat_added.append(self.rat_added)
        game.notify_rat.append(self.notify_rat)
        game.rat_dies.append(self.rat_dies)

        self.game.rat_added(self)

    def __exit__(self, *args, **kwargs):
        self.game.rat_dies(self)

    def __enter__(self):
        return self

    def rat_added(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1

    def rat_dies(self, which_rat):
        self.attack -= 1


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
